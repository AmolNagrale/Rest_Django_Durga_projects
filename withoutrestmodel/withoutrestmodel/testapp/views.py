from django.http.response import HttpResponse
# from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
# from django.core.serializers import serialize
from testapp.mixins import SerializeMixin, HttpResponseMixin
import json


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm

class EmployeeDetailCBV(SerializeMixin, HttpResponseMixin, View): # for the one Employee information
    def get(self,request, id, *args, **kwargs):
        try:
            emp=Employee.objects.get(id=id)# if we want to provide id explicitely not a hardcoded in program in that case we have directly id mension in
        except Employee.DoesNotExist:
            json_data=json.dumps({'emp':'The requested resourse data done not available'})
            return HttpResponse(json_data, content_type='application/json',status=404)
            #return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.serialize([emp,])
            return self.reder_to_http_response(json_data)



class EmployeeListCBV(SerializeMixin,HttpResponseMixin, View): # for the all Employee information
    def get(self,request,*args, **kwargs):
        qs=Employee.objects.all()  # for all the records
        # json_data=serialize('json',qs, fields=('eno','ename','eaddr')) # fields which is used to get perticular data & exclude rest of data.
        json_data=self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.reder_to_http_response(json_data, status=400)
        empdata=json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resourse Created Successfully !!'})
            return self.reder_to_http_response(json_data, status=400)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.reder_to_http_response(json_data,status=400)





