from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from testapp.serializers import NameSerializer
# Create your views here.

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy Pongal','colors':colors})

    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, Happy Pongal !!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializers.errors, status=400)
    
    def put(self,request,*args,**kwargs):
        return Response({'msg':'This response from put method of APIViews'})

    def patch(self,request,*args,**kwargs):
        return Response({'msg':'This response from patch method of APIViews'})

    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This response from delete method of APIViews'})


from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy New Year','colors':colors})

    def create(self, request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, Happy New Year 2022 !!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializers.errors, status=400)

    def retrive(self,request, pk=None):
        return Response({'msg':'This is the response of retrive method of ViewSet'})

    def update(self,request, pk=None):
        return Response({'msg':'This is the response of update method of ViewSet'})

    def partial_update(self,request, pk=None):
        return Response({'msg':'This is the response of partial_update method of ViewSet'})

    def destroy(self,request, pk=None):
        return Response({'msg':'This is the response of destroy method of ViewSet'})

    