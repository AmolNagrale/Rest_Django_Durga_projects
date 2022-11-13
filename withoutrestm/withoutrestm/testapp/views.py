from django.shortcuts import render
from django.views.generic import View
import requests
from requests import status_codes
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize

from testapp.mixins import SerializeMixin, HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin, SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
        data=request.body       # get the client provided data
        valid_json=is_json(data)  # if given data is not valid then please provide valid json data only 
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data) # if data is valid then convert it into python dictionary
        id=pdata.get('id',None) # check id is available or not 
        if id is not None:      
            emp=self.get_object_by_id(id) # if id is avilable then identify corresponding employee object 
            if emp is None:      
                json_data=json.dumps({'msg':'The reqested employee is not available with matched data'}) # if object is not available send request for correct data
                return self.render_to_http_response(json_data, status=404)
            json_data=self.serialize([emp,])   # if object is available then send json data to our partner application
            return self.render_to_http_response(json_data)
        qs = Employee.objects.all() # if id is None the queryset 
        json_data = self.serialize(qs) # & convert into json 
        return self.render_to_http_response(json_data) # send that json to partner application




# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):

    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp =None
        return emp

    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'requested json data is not available'})
            # return HttpResponse(json_data,content_type='application/json', status=404)
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.serialize([emp,])
        # return HttpResponse(json_data,content_type='application/json', status=200) # json data is apply on partner application
            return self.render_to_http_response(json_data)

    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'No matched resourse found, Cant perform update operation '})
            return self.render_to_http_response(json_data,status=404)   
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)

        provided_data=json.loads(data)

        original_data= {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }

        original_data.update(provided_data) # performing dict update operation 
        form=EmployeeForm(original_data, instance=emp) # instance is to allocate the old object
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resourse updated successfully'})
            return self.render_to_http_response(json_data, status=200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'No matched resourse found, Cant perform update operation '})
            return self.render_to_http_response(json_data,status=404)
        status, deleted_item = emp.delete()
        if status==1:
            json_data=json.dumps({'msg':'Resourse deleted successfully '})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'Unable to delete record, Please try again !! '})
        return self.render_to_http_response(json_data)

#===========================================================================================================

# @method_decorator(csrf_exempt, name='dispatch')
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin, View):
    
#     def get(self,request,*args,**kwargs):
#         print('***** GET ALL ******')
#         qs = Employee.objects.all()
#         json_data=self.serialize(qs)
#         return HttpResponse(json_data,content_type='application/json') # json data is apply on partner application

#     def post(self,request,*args,**kwargs):
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'Please send valid json data only'})
#             return self.render_to_http_response(json_data,status=400)
#         empdata=json.loads(data)
#         form=EmployeeForm(empdata)

#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Resourse created successfully'})
#             # return HttpResponse(json_data)
#             #return self.reder_to_http_response(json_data, status=200)
#             return self.render_to_http_response(json_data, status=200)

#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)

 

       

 
