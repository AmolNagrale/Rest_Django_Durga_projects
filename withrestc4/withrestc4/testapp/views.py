from django.shortcuts import render
# from rest_framework.utils import serializer_helpers
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from testapp.permissions import IsReadOnly, SunnyPermission, IsGETOrPatch
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testapp.authentications import CustomAuthentication, CustomAuthentication2

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #authentication_classes=[TokenAuthentication,]
    #authentication_classes=[CustomAuthentication,]
    authentication_classes=[CustomAuthentication2,]
    # authentication_classes=[JSONWebTokenAuthentication,]

    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
    permission_classes=[IsAuthenticated,]