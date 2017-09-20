class C2F:
    def __new__(cls, self):
        self = self*33.8
        return self.__new__()
    def __init__(self):
        print(self)
print(C2F(32))
