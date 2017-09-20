# a.py
import b

def x():
    print('x')

b.y()

# b.py
import a

def y():
    print('y')

a.x()
x'