from django.db import models

# Create your models here.


class Departments(models.Model):
    Department_Id = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.Department_Id}, {self.Department_Name}"


class Employees(models.Model):
    Employee_Id = models.AutoField(primary_key=True)
    Employee_Name = models.CharField(max_length=100)
    Employee_Dept = models.CharField(max_length=100)
    Employee_DOJ = models.DateField()
    Employee_PHOTO = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.Employee_Id}, {self.Employee_Name}, {self.Employee_Dept}, {self.Employee_DOJ}, {self.Employee_PHOTO}"