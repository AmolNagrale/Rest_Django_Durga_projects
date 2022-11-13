from django.shortcuts import render
import requests # we can send request to module
# Create your views here.
def get_geographic_info(request):
    
    ip=request.META.get('HTTP_X_FORWARDED_FOR','') or request.META.get('REMOTE_ADDR')
    url='http://api.ipstack.com/103.149.197.11?access_key=b05b0cccd06c5fc3738c6d66f8695567&format=1'
    #url='http://api.ipstack.com/'+str(ip)+'?access_key=b05b0cccd06c5fc3738c6d66f8695567&format=1'
    response=requests.get(url)
    data=response.json()
    return render(request, 'testapp/info.html',data)

