from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField

# Create your models here.
class Employee (models.Model):
    eno=IntegerField()
    ename=CharField(max_length=64)
    esal=FloatField()
    eaddr=CharField(max_length=64)