from django.shortcuts import render
from judge.models import user
from .models import jud_emp, employee
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import logging
from xlwt import *
from io import StringIO, BytesIO
import time


# Create your views here.
def index(request):
    return render(request, 'pub/index.html')


def showgrade(request, id):
    # 获取评委列表
    judge = user.objects.all()
    # 获取与该选手的相关的成绩
    grade = jud_emp.objects.filter(emp_id_id=id)

    for i in judge:
        for j in grade:
            if i == j.jud_id:
                i.grade = j.grade
    # 查找上一个下一个的id
    emp = employee.objects.all().order_by('num')
    id = int(id)
    pre = id - 1
    last = id + 1
    if last > emp.count():
        last = 99
    # 修改ONPAGE
    emp = employee.objects.get(id=id)
    settings.ONPAGE = int(id)
    return render(request, 'pub/showgrade.html', {'judge': judge, 'pre': pre, 'last': last, 'id': id, 'emp': emp})


def ajax_search(request):
    id = request.GET['emp_id']
    list = jud_emp.objects.filter(emp_id_id=id).order_by('jud_id_id')
    idlist = []
    gradelist = []
    for i in list:
        idlist.append(i.jud_id_id)
        gradelist.append(i.grade)
    logging.debug(idlist, gradelist)
    data = {'idlist': idlist, 'gradelist': gradelist}
    return JsonResponse(data)


def ajax_ave(request):
    id = request.GET['id']
    # 查看ave是否存在
    emp = employee.objects.get(id=id)
    # if (emp.ave_grade is not None) or(emp.ave_grade == 0):
    # 存在则取出，返回
    # 若不存在进行计算，写入
    #    ave = emp.ave_grade
    # else:
    list = jud_emp.objects.filter(emp_id_id=id).order_by('grade')
    sum = 0
    if len(list) > 2:
        for i in range(1, len(list) - 1):
            sum = sum + list[i].grade
        ave = sum / (len(list) - 2)
    else:
        for i in list:
            sum = sum + i.grade
        ave = round(sum / len(list), 2)
    ave = round(ave, 2)
    emp = employee.objects.get(id=id)
    emp.ave_grade = ave
    emp.save()
    minn = list[0].grade
    maxn = list[len(list)-1].grade
    data = {'ave': ave, 'max': maxn, 'min': minn}
    print(data)
    return JsonResponse(data)


def list(request):
    emp = employee.objects.all().order_by('num', 'id')
    settings.ONPAGE = 0
    return render(request, 'pub/list.html', {'emp': emp})


def sort(request):
    emp = employee.objects.all()
    for i in emp:
        if i.ave_grade is not None and i.papergrade is not None:
            i.totalgrade = float(i.ave_grade) * 0.7 + float(i.papergrade) * 0.3
            i.totalgrade = round(i.totalgrade, 2)
            i.save()
    emp = employee.objects.all().order_by('-totalgrade', '-papergrade')
    j = 1
    for i in emp:
        i.sort = j
        j = j + 1
    settings.ONPAGE = 0
    return render(request, 'pub/sort.html', {'emp': emp})


def base(request):
    return render(request, 'pub/base.html')


# 返回当前时间
def GetNowTime():
    return time.strftime("_%Y%m%d_%H%M%S", time.localtime(time.time()))


def excel_export(request):
    '''
    导出excel
    :param request:
    :return:
    '''
    emp = employee.objects.all().order_by('-totalgrade', '-papergrade')
    # 创建工作簿
    ws = Workbook(encoding='utf-8')
    w = ws.add_sheet('成绩单')
    w.write(0, 0, '排名')
    w.write(0, 1, '姓名')
    w.write(0, 2, '笔试成绩')
    w.write(0, 3, '业务展示成绩')
    w.write(0, 4, '总成绩')
    # 写入数据
    excel_row = 1
    i = 1
    for e in emp:
        w.write(excel_row, 0, i)
        w.write(excel_row, 1, e.name)
        w.write(excel_row, 2, e.papergrade)
        w.write(excel_row, 3, e.ave_grade)
        w.write(excel_row, 4, e.totalgrade)
        excel_row = excel_row + 1
        i = i + 1
    # 保存
    stime = GetNowTime()
    sfile = "成绩单" + stime + ".xls"
    #  文件存一份在服务器
    ws.save('./excel/' + sfile)
    sio = BytesIO()
    print(sio)
    ws.save(sio)
    sio.seek(0)

    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=grade.xls'
    response.write(sio.getvalue())
    return response


def showall(request, id, last):
    emp = employee.objects.get(id=id)
    if emp.ave_grade is not None and emp.totalgrade is not None:
        emp.totalgrade = emp.ave_grade * 0.7 + emp.papergrade * 0.3
        emp.save()
    last = int(last)
    return render(request, 'pub/showAll.html', {'id': id, 'last': last, 'emp': emp})
