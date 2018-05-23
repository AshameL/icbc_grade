from django.shortcuts import render
from judge.models import user
from .models import jud_emp, employee
from django.http import JsonResponse, HttpResponse


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
    # print(emp.count())
    if last > emp.count():
        last = -1
    # print('last:', last)
    return render(request, 'pub/showgrade.html', {'judge': judge, 'pre': pre, 'last': last, 'id': id})


def ajax_search(request):
    id = request.GET['emp_id']
    list = jud_emp.objects.filter(emp_id_id=id).order_by('jud_id_id')
    idlist = []
    gradelist = []
    for i in list:
        idlist.append(i.jud_id_id)
        gradelist.append(i.grade)
    print(idlist, gradelist)
    data = {'idlist': idlist, 'gradelist': gradelist}
    return JsonResponse(data)


def ajax_ave(request):
    id = request.GET['id']
    list = jud_emp.objects.filter(emp_id_id=id).order_by('grade')
    sum = 0
    if len(list) > 2:
        for i in range(1, len(list) - 1):
            sum = sum + list[i].grade
        ave = sum / (len(list) - 2)
    else:
        for i in list:
            sum = sum + i.grade
        ave = sum / len(list)
    return HttpResponse(ave)


def list(request):
    emp = employee.objects.all().order_by('num', 'id')
    return render(request, 'pub/list.html', {'emp': emp})


def sort(request):
    emp = employee.objects.all().order_by('totalgrade', 'ave_grade')
    return render(request, 'pub/sort.html', {'emp': emp})


def base(request):
    return render(request, 'base.html')
