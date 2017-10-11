import numpy as np
from cmath import *
import math

'''
Solving a system of linear equations in the form of A * x = B
1. Cholesky factorization of matrix A
2. Solving the equation A * x = B using Cholesky factorization

Input: matrices A, B
Output: Lower, upper triangular matrix for A and x 
'''

A = np.array([[0.05, 0.07, 0.06, 0.05], [0.07, 0.10, 0.08, 0.07], [0.06, 0.08, 0.10, 0.09], [0.05, 0.07, 0.09, 0.10]])
B = np.array([0.23, 0.32, 0.33, 0.31])

# Lower triangular matrix (Upper triangular matrix is the transpose of lower triangular matrix)
lower = np.zeros((4, 4))

# Cholesky factorization implementation
for k in range(4):
    temp_sum = 0
    if k == 0:
        lower[k][k] = math.sqrt(A[k][k])
    else:
        for s in range(k):
            temp_sum += lower[k][s]**2
        lower[k][k] = math.sqrt(A[k][k] - temp_sum)

    for i in range(k+1, 4):
        sum = 0
        if k == 0:
            lower[i][k] = A[i][k] / lower[k][k]
        else:
            for s in range(k):
                sum += lower[i][s]*lower[k][s]
            lower[i][k] = (A[i][k] - sum)/lower[k][k]

print("Lower triangular matrix, L \n", lower)
print("\n")
print("Upper triangular matrix U (transpose of L) \n", lower.transpose())
print("\n")
'''
Solving the below equation in 2 steps:
Lower * lower_transpose * x = B
1. Lower * z = B
2. lower_transpose * x = z
'''
z = np.linalg.solve(lower, B)
x = np.linalg.solve(lower.transpose(), z)
print("Solution to A * x = B \n", x)


