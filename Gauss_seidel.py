# Convergence is only guaranteed if the matrix is either diagonally dominant,
# or symmetric and positive definite

import numpy as np
'''
Solving the system of linear equations , Ax = B
Input:
A, B
Output:
x
'''
A = np.random
B = np.random
case = int(input("Select 1 or 2: "))
if case == 1:
    A = np.array([[3, 1, 1], [1, 3, -1], [3, 1, -5]])
    B = np.array([5, 3, -1])
    print("\n3x + y + z = 5\nx + 3y -z = 3\n3x + y - 5z = -1\n")
elif case == 2:
    A = np.array([[3, 1, 1], [3, 1, -5], [1, 3, -1]])
    B = np.array([5, -1, 3])
    print("\n3x + y + z = 5\n3x + y - 5z = -1\nx + 3y -z = 3\n")

n = B.shape[0]
X = np.zeros((n, 1))

# Check for diagonal dominance
diagonal_dominance_flag = 0
k = 0

for i in range(n):
    for j in range(n):
        if abs(A[i, j]) < abs(A[i, i]):
            k += 1

if k == n*(n - 1):
    diagonal_dominance_flag = 1

# Check for symmetric
symmetric_flag = 0
if np.array_equal(A, A.transpose()):
    symmetric_flag = 1

# Check for positive definite
positive_definite_flag = 0
if symmetric_flag == 1:
    V = np.ones((n,1))
    if np.dot(V.transpose(), np.dot(A, V)) >0:
        print("A is a positive definite")
        positive_definite_flag = 1

if diagonal_dominance_flag != 1 and positive_definite_flag!=1:
    print("Gauss Seidel method does not convergence (A is neither diagonally dominant nor positive definite)")

else:
    # Guass Siedel implementation
    iterations = int(input("No. of iterations:"))
    for k in range(iterations):
        for i in range(n):
            sum_prev = 0
            for j in range(n):
                if j != i:
                    sum_prev = sum_prev + A[i, j] * X[j, 0]
            X[i, 0] = (1/A[i, i]) * (B[i] - sum_prev)

    # Solution to linear system of equations
    print("\nSolution matrix X \n", X)

