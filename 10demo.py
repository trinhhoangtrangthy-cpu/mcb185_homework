print('hello world')

# 10demo.py by Thy Trinh
print('hello, again')

"""
This is a 
multiline comment
"""
import math

#Math 
print(1.5e-2)

print(1+1)
print(2**3)
print(pow(2,3))
print(math.pow(2,3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))

print(0.1*1)
print(0.1*3)

#Variables
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

#Type
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=',', end='!\n')

#Functions
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

hyp = pythagoras(3,4)
print(hyp)

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))

#Function Practice

def circle_area(r): return math.pi * r**2
print(circle_area(2))

def rectangle_area(w, h): return w * h
print(rectangle_area(2,3))

#Practice

def temp_convert(c): 
    f = c * 9/5 + 32
    return f
print(temp_convert(24))

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d
print(distance(0,0,3,4))

#Strings
s = 'hello world'
print(s, type(s))




    