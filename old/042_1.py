class Nstr(str):
    def __init__(self,x):
        self.x = x
    def __lshift__(self, other):
        return self.x[other:] +self.x[:other]
    def __rshift__(self, other):
        return self.x[:other]+self.x[other:]
a = Nstr('I love FishC.com!')
print(a << 3)
print(a >> 3)

