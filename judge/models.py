from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30, unique=True)
    num = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True)
    online = models.BinaryField()
