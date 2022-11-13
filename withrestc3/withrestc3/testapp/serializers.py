from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer
from testapp.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'