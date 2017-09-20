class Nstr(str):
    def __init__(self,x):
        self.x = 0
        for i in x:
            self.x += ord(i)
    def __add__(self, other):
        return self.x + other.x
    def __sub__(self, other):
        return self.x - other.x
    def __mul__(self, other):
        return self.x * other.x
    def __truediv__(self, other):
        return self.x / other.x
    def __floordiv__(self, other):
        return self.x // other.x
a = Nstr('FishC')
b = Nstr('love')
print(a+b,a-b,a*b,a/b,a//b)

