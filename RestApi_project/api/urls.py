
from django.urls import path
from . import views
urlpatterns = [
    path('',views.employeeList,name="api-employeelist"),
    path('detail/<str:pk>',views.employeeDetail,name="employee-detail"),
    path('create/',views.employeeCreate,name='api-employeecreate'),
    path('delete/<str:pk>',views.employeeDelete,name="employee-delete"),
    path('update/<str:pk>',views.employeeUpdate,name="employee-Update"),
]