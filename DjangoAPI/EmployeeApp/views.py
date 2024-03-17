from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializer import DepartmentSerializers, EmployeeSerializers



# Create your views here.
@csrf_exempt
def departmentAPI(request, id=0):
    if request.method=='GET': # get method we will return al the records in json fromat
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializers(departments, many=True) 

        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method=='POST': #it is used to insert new record into departments table
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializers(data=departments_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method=="PUT": #if we want to update the record
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(Department_ID=department_data['Departmet_Id'])

        departments_serializer = DepartmentSerializers(department, data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successful.", safe=False)
        
        return JsonResponse("Failed to update.")
    
    





