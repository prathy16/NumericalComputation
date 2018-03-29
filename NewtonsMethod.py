import math
from mpmath import *
'''
Input: 
Initial value x0, to start with
M - No of iterations
Case - To select a function among x - math.tan(x), x**3 - 5*x**2 + 3*x -7
Output: 
Root of the specific function
'''


# Choosing function based on user input, case
def func(x):
    if case == 1:
        return x - math.tan(x)
    else:
        return x**3 - 5*x**2 + 3*x -7


# Derivative function
def der(func, x):
    if case == 1:
        # Derivate of x - tan(x)
        return 1 - (sec(x))**2
    else:
        # Derivate of x**3 - 5*x**2 + 3*x -7
        return 3*x**2 - 10*x + 3


def newtons_method(x0):
    v = func(x0)
    # Stopping Condition
    if abs(v) <= epsilon:
        return x0
    for k in range(1, M+1):
        x1 = x0 - (v/der(func, x0))
        v = func(x1)
        # Stopping conditions
        if abs(x1-x0) <= delta or abs(v) < epsilon:
            return x0
        x0 = x1
    return x0


case = int(input("Pick a function: "))
x0 = float(input("Enter initial value X0: "))
M = int(input("No of iterations: "))
epsilon = 2.22044604925e-16 # Machine epsilon for 64-bit system
delta = 2.22044604925e-16
print("Root at X0 =", x0, "is", newtons_method(x0))


