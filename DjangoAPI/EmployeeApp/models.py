from django.db import models

# Create your models here.


class Departments(models.Model):
    Department_Id = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=500)
    