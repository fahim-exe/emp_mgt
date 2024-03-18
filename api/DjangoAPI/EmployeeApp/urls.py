from django.urls import path, include
from django.conf.urls.static  import static
from django.conf import settings


from EmployeeApp import views


urlpatterns=[
    path('department', views.departmentAPI),
    path('department/<int:id>', views.departmentAPI),
    path('employee', views.employeeAPI),
    path('employee/<int:id>', views.employeeAPI),
    
    path('employee/savefile', views.SaveFile),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url(r'^deapartment$', views.departmentAPI),
#     url(r'^deapartment/([0-9]+)', views.departmentAPI), #the delete method will recieve dept id in there
    
# ]
