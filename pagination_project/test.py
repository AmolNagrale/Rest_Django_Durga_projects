from faker import *
from random import *
faker=Faker()
feno=randint(1001,9999)
fename=faker.name()
feasal=randint(10000,200000)
feaddr=faker.city()
print('Employee Number :',feno)
print('Employee Name :',fename)
print('Employee Salary :',feasal)
print('Employee Address :',feaddr)