from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from testapp.pagination import MyPagination,Mypagination2,Mypagination3
# Create your views here.

class EmployeeListView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    search_fields=('ename','eno')
    #search_fields=('^eno',)# starts with
    # search_fields=('=eno',) # exact match
    ordering_fields=('^ename','esal') #default_value = '__all__'
    
    
    
    
# Vanilla filtering

    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs






#pagination/limit/offset

# class EmployeeListView(generics.ListAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
    #pagination_class=PageNumberPagination
    #pagination_class=MyPagination
    #pagination_class=Mypagination2
    #pagination_class=Mypagination3
