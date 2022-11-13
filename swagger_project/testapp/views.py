from rest_framework.serializers import ModelSerializer
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=ModelSerializer
    queryset=Employee.objects.all()