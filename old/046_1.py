import time
class Record:
    def __init__(self,value=None,name=None):
        self.val = value
        self.name = name
    def __get__(self, instance, owner):
        with open('record.txt', 'a') as a:
            a.write('%s 变量于%s 被读取，%s = %s \n' % (self.name, time.asctime(), self.name, str(self.val)))
        return self.val
    def __set__(self, instance, value):
        with open('record.txt', 'a') as a:
            a.write('%s 变量于%s 被修改，%s = %s \n' %(self.name,time.asctime(),self.name , value))
            self.val = value
class Test:
    x = Record(10,'x')
    y = Record(8.8,'y')
