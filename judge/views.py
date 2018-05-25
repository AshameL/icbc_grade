from django.shortcuts import render
from pub.models import employee, jud_emp
from .models import user
from django.http import HttpResponse, HttpResponseRedirect
import logging
from django.conf import settings

# Create your views here.

'''
# 评委打分界面，获取选手个数
def index(request):
    emp = employee.objects.all().order_by('id')
    # 获取跟该用户有关的成绩，按顺序order_by('emp_id')
    grade = jud_emp.objects.filter(jud_id=1).order_by('emp_id_id')
    # 成绩的合并
    for i in emp:
        for j in grade:
            if i.id == j.emp_id_id:
                i.grade = j.grade
    return render(request, 'index.html', {'emp': emp})

    # ajax 进行打分提交
'''


def index(request):
    if request.method == 'GET':
        if settings.ONPAGE == 0:
            return render(request, 'index.html', {'timeout': '评分暂停'})
        else:
            judgerid = request.session['judgerid']
            emp = employee.objects.get(id=settings.ONPAGE)
            try:
                je = jud_emp.objects.get(jud_id_id=judgerid, emp_id=emp)
                return render(request, 'index.html', dict(emp=emp, grade=je.grade))
            except:
                return render(request, 'index.html', {'emp': emp})


def ajax_submit(request):
    if request.method == "GET":
        emp_id = int(request.GET.get("emp_id"))
        jud_id = int(request.GET.get("jud_id"))
        grade = float(request.GET.get("grade"))
        je = jud_emp(emp_id_id=emp_id, jud_id_id=jud_id, grade=grade)
        # 插入数据库
        try:
            tmp = jud_emp.objects.get(emp_id=emp_id, jud_id=jud_id)
            logging.error('评委已经打分，重复插入')
            return HttpResponse('请勿重复打分')
        except:
            try:
                je.save()
            except:
                logging.warning('评委打分未录入')
                return HttpResponse('评委打分失败，请联系管理员')
        logging.debug('评委打分成功！')
    return HttpResponse('评委打分成功！')


def ajax_reload(request):
    logging.debug('[reload]')
    page = request.GET['page']
    if int(settings.ONPAGE) == int(page):
        logging.info('[info]不会刷新', settings.ONPAGE, page)
        return HttpResponse('false')
    logging.info('[info]刷新', settings.ONPAGE, page)
    return HttpResponse('true')


# 登录
def login(request):
    if request.method == 'POST':
        logging.debug('登录验证')
        username = request.POST['username']
        password = request.POST['password']
        try:
            judger = user.objects.get(username=username, password=password)
            judger.online = 1
            judger.save()
            logging.debug('————评委用户online状态：1')
            request.session['judgerid'] = judger.id
            request.session['judgername'] = judger.name
            logging.debug('————登录成功')
            return HttpResponseRedirect('/judge/')
        except:
            logging.debug('————用户名密码错误')
            return render(request, 'login.html', {'error': '用户名密码错误'})
    return render(request, 'login.html')


def logout(request):
    id = request.session['judgerid']
    judger = user.objects.get(id=id)
    judger.online = 0
    judger.save()
    logging.debug('————评委用户online状态：0')
    del request.session['judgerid']
    del request.session['judgername']
    logging.debug('————评委用户session清空')

    return HttpResponseRedirect('/login/')


''''# websocket
@require_websocket
def start_server_script(request):
    # print('is websocket:'+ request.is_websocket())
    # for message in request.websocket:
    #     print(str(message,encoding = "utf-8"))
    #     sendmes = '我是服务器!'
    #     b = bytes(sendmes, encoding = "utf8")
    #
    #     request.websocket.send(b)
    a = '1'
    while request.websocket.read():
        print('读取中')
        t = onpage.objects.get(id=1)
        if a != t.thispage:
            print('改变了')

'''

def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '404.html')


def permission_denied(request):
    return render(request, '404.html')