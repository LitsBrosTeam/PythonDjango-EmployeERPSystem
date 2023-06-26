from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(default=1,primary_key=True)
    empname = models.CharField(max_length=200)
    empemail = models.CharField(max_length=200)
    empmobile = models.CharField(max_length=20)
    empdesignation  = models.CharField(max_length=200)
    empsalary = models.IntegerField()
