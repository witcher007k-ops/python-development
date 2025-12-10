import numpy as np

def get_matrix(n, m):
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

print("Matrix Operations Tool")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")

choice = int(input("Choose an operation: "))

if choice in [1, 2, 3]:
    r1 = int(input("Rows of Matrix A: "))
    c1 = int(input("Columns of Matrix A: "))
    A = get_matrix(r1, c1)

    r2 = int(input("Rows of Matrix B: "))
    c2 = int(input("Columns of Matrix B: "))
    B = get_matrix(r2, c2)

    if choice == 1:
        print("Result:\n", A + B)
    elif choice == 2:
        print("Result:\n", A - B)
    elif choice == 3:
        print("Result:\n", A @ B)

elif choice == 4:
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    A = get_matrix(r, c)
    print("Transpose:\n", A.T)

elif choice == 5:
    n = int(input("Matrix size (n x n): "))
    A = get_matrix(n, n)
    print("Determinant =", np.linalg.det(A))
