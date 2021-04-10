from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerilizer
from .models import Employee

@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerilizer(employees,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employeeDetail(request,pk):
    employees = Employee.objects.get(id=pk)
    serializer = EmployeeSerilizer(employees,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def employeeUpdate(request,pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerilizer(instance=employee,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def employeeDelete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()  
    return redirect('/api')