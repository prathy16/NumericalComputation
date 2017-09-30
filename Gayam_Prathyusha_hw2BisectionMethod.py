import numpy as np
import math
from mpmath import *

'''
Input:
Case: Picking a function from 
(1/x) - tan(x), 
(1/x) - 2**x,
x**8 - 36*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320
x**8 - 36.001*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320

Initial interval points [a, b]

M - maximum number of iterations

Output:
Root within that interval
'''

def func(x):
    if case == 1:
        # root of (1/x) - tan(x) is same as math.cos(x) - x*math.sin(x)
        return math.cos(x) - x*math.sin(x)
    elif case == 2:
        # root of (1/x) - 2**x is same as 1 - x*2**x
        return 1 - x * (2**x)
    elif case == 3:
        return x**8 - 36*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320
    else:
        return x**8 - 36.001*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320


def bisection_method(a, b, iteration):
    c = (a + b) / 2.0
    if iteration < M:
        iteration += 1
        if np.sign(func(a))*np.sign(func(c)) < 0:
            return bisection_method(a, c, iteration)
        elif np.sign(func(c))*np.sign(func(b)) < 0:
            return bisection_method(c, b, iteration)
        else:
            return c
    else:
        return c


case = int(input("Pick a function f: "))
a = float(input("Enter interval point a: "))
b = float(input("Enter interval point b: "))
M = int(input("Max iterations: "))
iteration = 0
print("Root within [",a,",",b,"] is:",bisection_method(a, b, iteration))
