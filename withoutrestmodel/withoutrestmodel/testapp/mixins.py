from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self,qs): # instate of serialize we can can use any name just need to same name call at views.py def
        json_data=serialize('json',qs)
        final_data=[]
        p_data=json.loads(json_data)
        for obj in p_data:
            emp_data=obj['fields'] # this code to get the value against fields key
            final_data.append(emp_data)
        json_data=json.dumps(final_data)
        return json_data



from django.http import HttpResponse
class HttpResponseMixin(object):
    def reder_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data, content_type='application/json',status=status)