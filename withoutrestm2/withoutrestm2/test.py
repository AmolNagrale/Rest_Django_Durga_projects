import requests 
import json
BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+END_POINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource()



# def create_resource():
#     new_std={
#         'name':'k1',
#         'rollno':888,
#         'marks':54,
#         'gf':'kk',
#         'bf':'kkkk'
#     }
#     r=requests.post(BASE_URL+END_POINT,data=json.dumps(new_std))
#     print(r.status_code)
#     print(r.json)
# create_resource()


def update_resource(id):
    new_data={
        'id':id,
        'marks':33,
        'gf':'mm'

    }

#     r=requests.put(BASE_URL+END_POINT,data=json.dumps(new_data))
#     print(r.status_code)
#     print(r.json())
# update_resource(4)


def delete_resource(id):
    data={
        'id':id,
    }
    r=requests.delete(BASE_URL+END_POINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
delete_resource(6)