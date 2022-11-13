from django.conf.urls import url
import requests, json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resourse(id=None):
    data={} # if u r passing id then perticular record display else all record will display
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    # print(resp.status_code)
    print(resp.json()) 
get_resourse(5)

#########################CRUD Operation ##############################

# # This code for the get request only
# def get_resource(id):
#     resp=requests.get(BASE_URL+ENDPOINT+'/')
#     # if resp.status_code in range(200,300):
#     if resp.status_code ==requests.codes.ok:
#         print(resp.json())
#     else:
#         print('something goes wrong !!')
# id=input('Enter the id :')
# get_resource(id)

# #========================================

# import json

# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# get_all()

#============================================================
# this is the post record operation(create)

# def create_resource():
#     new_emp={
#         'eno':'900',
#         'ename':'Shardul',
#         'esal': 1000,
#         'eaddr':'Gujrat'
#     }
#     #print('----> ',json.dumps(new_emp))
#     resp=requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
#     print(resp.json())
#     print(resp.request.body)
#     print(resp.status_code)
    
# # create_resource()
# # print('Resourse created successfully !!')

# #===============================================================

# # This is the put opration

# def update_resource(id):
#     new_emp={
        
#         'ename':'Abdul',
#         'esal': 40,
        
#     }
#     resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=json.dumps(new_emp))
#     print(resp.json())
#     # print(resp.request.body)
#     print(resp.status_code)
    
# # update_resource(43)
# # print('Resourse updated successfully !!')

# #=================================================================
# # this is the delete operation 
# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.json())
#     print(resp.status_code)
    
# delete_resource(31)
# # print('Resourse updated successfully !!')