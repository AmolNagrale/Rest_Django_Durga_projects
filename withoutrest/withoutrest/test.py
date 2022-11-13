import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijsoncbv'
# r=requests.get(BASE_URL+ENDPOINT)
# r=requests.post(BASE_URL+ENDPOINT+'/') # +'/' is ipmortant to post the data otherwise we will get the set APPEND_SLASH=False error
# r=requests.put(BASE_URL+ENDPOINT+'/')
r=requests.delete(BASE_URL+ENDPOINT)
data=r.json()
# print('Data from django Application')
# print('#'*30)
# print('Employee Number :',data['eno'])
# print('Employee Name :',data['ename'])
# print('Employee Salary :',data['esal'])
# print('Employee Address :',data['eaddr'])
print(data)
# print(r.text)