#Object Serialization:
#To process of converting an object from python supported form to file supproted form or network suppoerted form,is  called seralization(marsheling or pickling)
#we need required picke moduel
#Deserialization:
# To process of converting  obect from file supported form or network supported form to python supported form ,is call Deserialization(unpickling and unmasrshing)
# we have to convert  python object from python application form to java application form or mobile application form,is called also serialization
# java application or mobile application can't understand python objecet that way we need to Json or YAML 
# 1.Object serialization by using pickle
# 2.object serialization by using JSON
# 3.Object serialization by using YAML


#1.Object serialization and deserialization by using pickle:
# we can perform serialization and deserialization of an object with respect to file by using pickle module.it is python inbuilt module
#pickle module conatins dump() function to perform serialization(picking).
#pickle.dump(object,file)
#pickle module contain load() function to perform deserialization(unpickling)
#object=pickle.load(file)
# To convert python object to file used dump function
#e=Employee(100.'durga',1000),'hyd')
#with open ('emp.txt','wb') as f:
#pickle.dump(e,f)

#with open('emp.txt','rd') as f:
#pickle.load(f)


#Program to Perform pickiling and unpickling of Employee Object
import pickle
from typing import Literal
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=Employee(100,'subbu',1000,'Bang')
with open('emp.txt','wb') as f:
    pickle.dump(e,f)
print('pickling Employee object sucessfulluy')
with open('emp.txt','rb') as f:
    newobj=pickle.load(f)
#print('unpickling Employee object completed')
print('Printing Employee object ')
newobj.display()


#2.object serilazition by using JSON:
#-----------------------------------
#Json=javascript object notation
# the most commanly use message format for application irrspective language
# Any programming language can understand json. Hense json is the most commnly used message format irrespectuly language
#eg:
# java application send request to python apllication.python application provide required response
#in json form.Java application can understand json form and can use based on requi
#int---number
#float----number
#list----array
#dict---object
#str---string
#True---true
#False--false
#JSON===Javascript Object Notation
#jSON is similar to  python dict  object
# Note:in olden days ,we used very common message format is xml which is very weight
# But these days everone preferring Json because of light weight
# Json module:
# ------------
# As the part of programming requirement, it is very common requirement to convert python object into..
# json form and from json from to python object.
# For these conversions(serialization and Deserialization)Python provides inbuilt module json.

# For Serialization Purpose(From Python to JSON Form):
#----------------------------------------------------- 
#1.dumps()--->It serializes python dict object to json string.
#2.dump()---->Converting python dict object to json and write that json to provided json file.it serialization to afile
#Employee object---->python dict---->json
#For Deserialization Purpose(From json form to Python form):
#-----------------------------------------------------------
#1.loads()-->Converting Json string to pyton dict.It deserialization to astring
#2.load()--->Reading json from afile and converting to python dict object .Deserializes from a json file.
#json---->python dict---->employee object
#Demo program for  serializtion

import json
employee={'name':'subbu',
        'age':30,
        'salary':1000,
        'ismarried':True,
        'ishavingGF':None
         }
json_string=json.dumps(employee,indent=4)
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)

#Demo program for Deserilazitaion
#'''      '''------>multline sting Literal
import json
json_string='''{
    "name": "subbu",
    "age": 30,
    "salary": 1000,
    "ismarried": true,
    "ishavingGF": null
}'''
emp_dict=json.loads(json_string)
print(type(emp_dict))
print('Employee Name:',emp_dict['name'])
print('Employee Age:',emp_dict['age'])
print('Employee Salary:',emp_dict['salary'])
print('Employee IsMarried:',emp_dict['ismarried'])
print('is Employee has GF:',emp_dict['ishavingGF'])
#or
for k,v in emp_dict.items():
    print('{} : {}'.format(k,v))


import json
with open('emp.json','r') as f:
    emp_dict=json.load(f)

print(type(emp_dict))
print('Employee Name:',emp_dict['name'])
print('Employee Age:',emp_dict['age'])
print('Employee Salary:',emp_dict['salary'])
print('Employee IsMarried:',emp_dict['ismarried'])
print('is Employee has GF:',emp_dict['ishavingGF'])
#or
for k,v in emp_dict.items():
    print('{} : {}'.format(k,v))


import json
with open('market.txt','r') as f:
    mart_info=json.load(f)
for k,v in mart_info.items():
    print('{}:{}'.format(k,v))
print()

#From python application how to send http request
#we need request module
# pip install request
#import json Here no nedd to json model because not using json function
import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(type(response))
bitcoininfo=response.json()
print(type(bitcoininfo))
print(bitcoininfo)
print('Bitcoin price as on:',bitcoininfo['time']['updated'])
print('In USD:',bitcoininfo['bpi']['USD']['rate'])


print()

#How to convert our customized object like Employee object to json:
#------------------------------------------------------------------

#Serialization and Deserilaization by using jsonpickle module
#note: we cant convert directly employee object to json
# By using jsonpickle module we can serialaization our custom class object to json and
# we can deserialization json to our cutom class object directly
#jsonpickle module is not available bydefault and we have to install explicitly
# pip install jsonpickle  
#json pickle module contain the following function to perform serialaization and Deserilazition
#1.encode()====>To vonvert any object to json_string directly
#2.decode()===>To convert json_string to our original object
import jsonpickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr,ismarried):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
        self.ismarried=ismarried
    def display(self):
        print('ENO:{},ENAME:{},ESAL:{},EADDR:{},ISMARRIED:{}'.format(self.eno,self.ename,self.esal,self.eaddr,self.ismarried))
e=Employee(100,'subbu',10000,'bang',True)
#Serialization to json string we use endoce () function
json_string=jsonpickle.encode(e)
print(json_string)

#Serialization to json file
with open('emp1.json','w') as f:
    f.write(json_string)

#Deserilazation from json string to employee object we used decode () function
e2=jsonpickle.decode(json_string)
e2.display()

print()
#Deserialization fro json file to employee object
with open ('emp1.json','r') as f:
    json_file=f.readline()
e3=jsonpickle.decode(json_file)
e3.display()


#3.Serialaztion by using YAML 
import yaml

employee={'name':'subbu',
        'age':30,
        'salary':1000,
        'ismarried':True,
        'ishavingGF':None
         }
with open('text.yaml','w') as f:
    yaml.dump(employee,f)


#Deserialixation of from yaml to python object

with open('text.yaml') as f:
    ya_string=yaml.safe_load_all(f)
    print(type(ya_string))
    print(next(ya_string))



