from django.contrib import admin
from .models import employee, jud_emp
from judge.models import user


# Register your models here.


@admin.register(employee)
class employeeAd(admin.ModelAdmin):
    list_display = ('id', 'name', 'ave_grade', 'papergrade', 'totalgrade')


@admin.register(jud_emp)
class jud_empAd(admin.ModelAdmin):
    list_display = ('id', 'emp_id_id', 'jud_id_id', 'grade')


@admin.register(user)
class userAd(admin.ModelAdmin):
    list_display = ('id', 'username', 'num', 'name')
