import numpy as np
def solve_linear_system(A, B):
    print("Menyelesaikan SPL Ax = B menggunakan metode matriks balikan.")
    print("A: Matriks koefisien (n x n)")
    print("B: Vektor hasil (n x 1)")
    try:
        # Menghitung matriks balikan A
        A_inv = np.linalg.inv(A)
        
        # Mengalikan matriks balikan A dengan vektor hasil B
        X = np.dot(A_inv, B)
        
        return X
    except np.linalg.LinAlgError:
        return None  # Matriks A tidak memiliki balikan

A = np.array([[3, 2], [2, 1]])
B = np.array([[6], [5]])

# Menyelesaikan SPL
solution = solve_linear_system(A, B)

if solution is not None:
    x, y = solution.flatten()
    print(f"Solusi SPL: x = {x}, y = {y}")
else:
    print("Matriks koefisien tidak memiliki balikan.")

# Verifikasi solusi dengan mengalikan matriks A dengan solusi yang ditemukan
if np.allclose(np.dot(A, solution), B):
    print("Verifikasi berhasil: A * X = B")
else:
    print("Verifikasi gagal.")