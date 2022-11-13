import requests
import json
import time
BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'
def get_resource(id=None):
    print('Get Operation......')
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource()
time.sleep(5)



# def create_resource():
#     print('Post Operation.......')
#     new_emp={
#         'eno':'106',
#         'ename':'SaiTeja',
#         'esal':7000,
#         'eaddr':'J&K',
        
#     }
#     r=requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
#     print(r.status_code)
#     print(r.json)
# create_resource()
# time.sleep(10)


# def update_resource(id):
#     print('Put Operation.......')
#     new_data={
#         'id':id,
#         #'eno':105,
#         'ename':'Shiva Shankar Varma',
#         'esal':6000,
#         #'eaddr':'Chennai',

#     }

#     r=requests.put(BASE_URL+END_POINT,data=json.dumps(new_data))
#     print(r.status_code)
#     print(r.json())
# update_resource(2)
# time.sleep(15)

''' below output get after inserting partial data (means esal & eaddr), for the update we need to complate attribute of thr data

       400
{'eno': ['This field is required.'], 'ename': ['This field is required.']}'''

# def delete_resource(id):
#     print('Delete Operation.......')
#     data={
#         'id':id,
#     }
#     r=requests.delete(BASE_URL+END_POINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# delete_resource(9)
