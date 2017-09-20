import sys
sys.modules[__name__] = A()
class Const:
    def __setattr__(self, key, value):
        if key.isupper():
            super().__setattr__(key,value)
        else:
            raise TypeError
