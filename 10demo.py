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

#Conditionals 
a = 2
b = 2
if a == b:
    print('a equals b')
    print(a,b)

def is_even(x):
    if x % 2 ==0: return True
    return False

print(is_even(2))
print(is_even(3))

#Boolean
a = 2
b = 3
c = a == b
print(c, type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

#Boolean Chains 
if a < b or a > b: 
    print('all things being equal, a and b are not')
if a < b and a > b: 
    print('you are living in a strange world')
if not False: 
    print(True)

#Floating Point Warning
a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

#Floating Point Warning

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: 
    print('close enough')

if math.isclose(a, b): 
    print('close enough')
     
#String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: 
    print('A < B')
if s2 < s3: 
    print('B < a')

#Mismatched Type Error
a = 1
s = 'G'
if a < s: 
    print('a < s')

#None Type
def silly(m, x, b):
	y = m * x + b
	#return y

print(silly(2,3,4))

#Iteration
while True:
    print('hello')

i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break

i = 0
while i < 3:
    i = i + 1
    print('hey', i)

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

#for i in range()

for i in range(1, 10, 3): #range from 1 to 10, increment of 3
    print(i)

for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

for i in range(5):
    print(i)
for i in range(0, 5):
    print(i)
for i in range(0, 5, 1):
    print(i)

#Nesting
for i in range(7):
    if i % 2 ==0: print(i, 'is even')
    else: print(i, 'is odd')

#Iteration Practice Solutions

#triangular()
def triangular(n):
    tri = 0
    for i in range(n+1):
        tri = tri + i
    return tri

print(triangular(5))

#factorial()
def factorial(n):
    if n == 0: return 1
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac
    
print(factorial(0))

#poisson()
def poisson(n, k):
    return n**k * math.e**-n / factorial(k)

print(poisson(2,3))

#nchoosek()
def nchoosek(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))
print(nchoosek(5,2))

#euler()
def euler(n):
    e = 0
    for k in range(n):
        e = e + 1 / factorial(k)
    return e

print(euler(10))

#The principle for writing a function is to have (1) a range, (2) a starting point, and (3) variables that are updated in the loop.

#is_prime()

def is_prime(n):
    for i in range(2, n//2): #n//2 is floor division, which assigns the quotient of n and 2 to i, but rounds down to the nearest integer.
        if n % i == 0: return False
    return True

#nilakantha (not sure what's going on here)
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1): #why does limit have to be +1?
         n = 2 * i
         d = n * (n+1) * (n+2)
         if i % 2 == 0: pi = pi - 4/d
         else: pi = pi + 4/d
    return pi

print(nilakantha(100))

#Random Numbers
import random

for i in range(5):
    print(random.random())

for i in range(3):
    print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# += equals increment. Example: a += 1 is a = a + 1
# -= equals decrement. Example: a -= 1 is a = a - 1
# *= equals multiply. Example: a *= 2 is a = a * 2




