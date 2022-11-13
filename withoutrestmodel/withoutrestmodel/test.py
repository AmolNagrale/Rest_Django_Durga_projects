import requests, json
from requests.api import request
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_resource(id):
    # id=input('Enter some ID :')
    r=requests.get(BASE_URL+ENDPOINT+id+'/')
    #if r.status_code in range(200,300):
    if r.status_code ==requests.codes.ok:
    
        print(r.json())
    else:
        print('something goes wrong')
    print(r.status_code)
    # print(r.json())

def get_all():
    r=requests.get(BASE_URL+ENDPOINT)
    print(r.status_code)
    print(r.json())

def create_resourse(): # we can use any name instate of create resourse
    new_emp={
        "eno": 500,
        "ename": "Varun",
        "esal": 5000.0,
        "eaddr": "Mumbai"
    }
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json)
create_resourse()


