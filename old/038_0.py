import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def gener(self):
        return (self.x,self.y)
class Line:
    def __init__(self,point1,point2):
        self.line = math.sqrt(math.pow((point1[0]-point2[0]),2) + math.pow((point1[1]-point2[1]),2))
    def result(self):
        print('这条直线的长度为%.2f'% self.line)
a = Point(float(input('请输入A点的X坐标：')),float(input('请输入A点的Y坐标：')))
a = a.gener()
b = Point(float(input('请输入B点的X坐标：')),float(input('请输入B点的Y坐标：')))
b = b.gener()
line = Line(a,b)
line.result()
