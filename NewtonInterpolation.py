
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# f(x) = 1/(1 + x^2)
def func(k):
    return 1/(1+k*k)

n1 = int(input()) 
n2 = int(input())
n3 = int(input())

# Equally spaced points with h = (b-a)/n
h1 = 10/n1
h2 = 10/n2
h3 = 10/n3

# Each x1, x2, x3 stores the interpolation points
x1 = []
x2 = []
x3 = []

for i in range(n1):
    x1.append(-5+i*h1)
for i in range(n2):
    x2.append(-5+i*h2)
for i in range(n3):
    x3.append(-5+i*h3)


y1 = []
y2 = []
y3 = []

for i in x1:
    y1.append(func(i))
for i in x2:
    y2.append(func(i))
for i in x3:
    y3.append(func(i))

# Coefficients c0, c1, c2 .... for each n is computed using divided difference
mat1 = np.zeros((n1, n1))
mat2 = np.zeros((n2, n2))
mat3 = np.zeros((n3, n3))

for i in range(n1):
    for j in range(i+1):
        mat1[i, j] = 1
for i in range(1, n1):
    for j in range(1, i+1):
        for k in range(j):
            mat1[i, j] *= (x1[i] - x1[k])
            

for i in range(n2):
    for j in range(i+1):
        mat2[i, j] = 1
for i in range(1, n2):
    for j in range(1, i+1):
        for k in range(j):
            mat2[i, j] *= (x2[i] - x2[k])
        
for i in range(n3):
    for j in range(i+1):
        mat3[i, j] = 1
for i in range(1, n3):
    for j in range(1, i+1):
        for k in range(j):
            mat3[i, j] *= (x3[i] - x3[k])


# Ax = B is solved where matrix c is coefficient matrix            
c1 = np.linalg.solve(mat1, y1)
c2 = np.linalg.solve(mat2, y2)
c3 = np.linalg.solve(mat3, y3)

# new_x, new_y stores the 30 equally spaced points and their f(x)
new_x1 = []
new_y1 = []

new_x2 = []
new_y2 = []

new_x3 = []
new_y3 = []

# For 30 equally spaced points h = (5 - (-5))/30
new_h = 1/3

for i in range(30):
    new_x1.append(-5+i*new_h)
    new_y1.append(func(new_x1[i]))
    
for i in range(30):
    new_x2.append(-5+i*new_h)
    new_y2.append(func(new_x2[i]))
    
for i in range(30):
    new_x3.append(-5+i*new_h)
    new_y3.append(func(new_x3[i]))

# Each list_values stores the p(x) values
list_values1 = []
list_values2 = []
list_values3 = []

for i in range(30):
    p = c1[n1-1]
    for k in range(1,n1):
        p = c1[n1-k-1] + (new_x1[i] - x1[n1-k-1])*p
    list_values1.append(p)
    
for i in range(30):
    p = c2[n2-1]
    for k in range(1,n2):
        p = c2[n2-k-1] + (new_x2[i] - x2[n2-k-1])*p
    list_values2.append(p)
    
for i in range(30):
    p = c3[n3-1]
    for k in range(1,n3):
        p = c3[n3-k-1] + (new_x3[i] - x3[n3-k-1])*p
    list_values3.append(p)

# f(x) - p5(x)    
print('x1', x1)
for i in range(30):
    print(func(new_x1[i])-list_values1[i])

# f(x) - p10(x)
print('x2', x2)
for i in range(30):
    print(func(new_x2[i])-list_values2[i])

# f(x) - p10(x)
print('x3', x3)
for i in range(30):
    print(func(new_x3[i])-list_values3[i])


