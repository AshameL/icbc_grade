from django.shortcuts import render
from pub.models import employee, jud_emp
from django.http import HttpResponse
import logging


# Create your views here.


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


def ajax_submit(request):
    if request.method == "GET":
        emp_id = int(request.GET.get("emp_id"))
        jud_id = int(request.GET.get("jud_id"))
        grade = float(request.GET.get("grade"))
        je = jud_emp(emp_id_id=emp_id, jud_id_id=jud_id, grade=grade)
        logger = logging.getLogger('ajax_打分')
        # 插入数据库
        try:
            tmp = jud_emp.objects.get(emp_id=emp_id, jud_id=jud_id)
            logger.error('评委已经打分，重复插入')
            return HttpResponse('请勿重复打分')
        except:
            try:
                je.save()
            except:
                logger.warning('评委打分未录入')
                return HttpResponse('评委打分失败，请联系管理员')
        logger.debug('评委打分成功！')
    return HttpResponse('评委打分成功！')
