from django.contrib import admin
from .models import employee, jud_emp
from judge.models import user


# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = '长春支行现场评分管理平台'  # 此处设置页面显示标题
    site_title = '中国工商银行长春支行'  # 此处设置页面头部标题


@admin.register(employee)
class employeeAd(admin.ModelAdmin):
    list_display = ('id', 'name', 'ave_grade', 'papergrade', 'totalgrade')
    ordering = ('id',)


@admin.register(jud_emp)
class jud_empAd(admin.ModelAdmin):
    list_display = ('id', 'emp_id', 'jud_id', 'grade')
    ordering = ('id',)


@admin.register(user)
class userAd(admin.ModelAdmin):
    list_display = ('id', 'username', 'num', 'name')
    ordering = ('id',)
