import time
class Record:
def __init__(self,value,name):
self.val = value
self.name = name
with open('record.txt','w+') as a
def __get__(self, instance, owner):
a.write('%s 变量于%s 被读取，%s = %f' %(self.name,time.asctime(),self.name , self.val))
return self,val
def __set__(self,instance,value):
self.val = value
a.write('%s 变量于%s 被修改，%s = %f' %(self.name,time.asctime(),self.name , self.val))
