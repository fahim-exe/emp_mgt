from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializer import DepartmentSerializers, EmployeeSerializers
from django.core.files.storage import default_storage



# Create your views here.
#this api is used for department model of db

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
        department = Departments.objects.get(Department_Id=department_data['Department_Id'])

        departments_serializer = DepartmentSerializers(department, data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successful.", safe=False)
        
        return JsonResponse("Failed to update.")
    

    elif request.method=="DELETE":
        department = Departments.objects.get(Department_Id=id)
        department.delete()

        return JsonResponse("Deleted Successfully", safe=False)
    


#this api is used for employee model of db

@csrf_exempt
def employeeAPI(request, id=0):
    if request.method=='GET': # get method we will return al the records in json fromat
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializers(employees, many=True) 

        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method=='POST': #it is used to insert new record into departments table
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializers(data=employees_data)

        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method=="PUT": #if we want to update the record
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(Employee_Id=employees_data['Employee_Id'])

        employees_serializer = EmployeeSerializers(employees, data=employees_data)

        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successful.", safe=False)
        
        return JsonResponse("Failed to update.", safe=False)
    

    elif request.method=="DELETE":
        employee = Employees.objects.get(Employee_Id=id)
        employee.delete()

        return JsonResponse("Deleted Successfully", safe=False)
    


@csrf_exempt

def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)