from django.db import models
from django.db.models.base import Model

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=64)