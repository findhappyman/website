class Rectangle:
    long = 0
    width = 0
    def setRect(self):
        self.long = float(input('请输入长：'))
        self.width = float(input('请输入宽：'))
    def getRect(self):
        print('长是%.2f，宽是%.2f'%(self.long,self.width))
    def getArea(self):
        print('面积为%.2f'% (self.long*self.width))