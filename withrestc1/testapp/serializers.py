from rest_framework import serializers, validators
from testapp.models import Employee

def multiples_of_1000(value): # first priority
    print('Validation by validator attribute')
    if value %1000 !=0:
        raise serializers.ValidationError('Employee salary should be multiples of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal=serializers.FloatField(validators=[multiples_of_1000])
    class Meta:
        model=Employee
        fields='__all__'

# Normal serializer

# class EmployeeSerializer(serializers.Serializer):
#     eno=serializers.IntegerField()
#     ename=serializers.CharField(max_length=64) # by inbuild validator/ using validator fields if we are assiged 4 charecter instate of 64 & input we have taken <4 char then error raise
#     esal=serializers.IntegerField(validators=[multiples_of_1000])
#     eaddr=serializers.CharField(max_length=64)

#     def validate_esal(self,value):   # esal value 5000 & more than is accepted, if we are taking 4999 the get the status code 400 
#         print('field level validation') # second priority
#         if value <5000:
#             raise serializers.ValidationError('Employee salary should be minimum 5000')
#         return value

#     def validate(self,data): # third priority
#         print('Object level validation')
#         ename=data.get('ename')
#         esal=data.get('esal')

#         if ename.lower()=='sunny': # it sholud be accepted upper & lower case also
#             if esal<50000:
#                 raise serializers.ValidationError('Sunny salary should be 5000')
#         return data

#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance