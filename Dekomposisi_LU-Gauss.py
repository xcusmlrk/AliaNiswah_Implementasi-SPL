import numpy as np

def dekomposisi_lu_gauss(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in 
range(i))) / U[i, i]
    return L, U

def solve_system(A, b):
    L, U = dekomposisi_lu_gauss(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

# Example usage
A = np.array([[3, 2], [2, 1]])
b = np.array([6, 5])

solution = solve_system(A, b)
print("Solution:", solution)