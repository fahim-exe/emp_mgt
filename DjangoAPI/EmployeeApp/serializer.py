from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields = ('Department_ID', 'Department_Name')


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('Employee_ID', 'Employee_Name', 'Employee_Dept', 'Employee_DOJ', 'Employee_PHOTO')