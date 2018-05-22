from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    num = models.IntegerField(null=True)
    name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
