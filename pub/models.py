from django.db import models
from judge.models import user
from django.dispatch import receiver

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30)
    num = models.IntegerField(null=True)
    ave_grade = models.FloatField(null=True,blank=True)

    papergrade = models.FloatField(null=True,blank=True)
    totalgrade = models.FloatField(null=True,blank=True)


class jud_emp(models.Model):
    jud_id = models.ForeignKey(user)
    emp_id = models.ForeignKey(employee)
    grade = models.FloatField()


    class Meta:
        unique_together = ('jud_id', 'emp_id')

