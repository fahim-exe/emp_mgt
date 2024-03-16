from django.db import models

# Create your models here.


class Departments(models.Model):
    Department_Id = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=500)


class Employees(models.Model):
    Employee_Id = models.AutoField(primary_key=True)
    Employee_Name = models.CharField(max_length=100)
    Employee_Dept = models.CharField(max_length=100)
    Employee_DOJ = models.DateField()
    Employee_PHOTO = models.CharField(max_length=100)