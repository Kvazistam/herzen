import numpy as np


def lu_decomp(matrix):
    n = len(matrix)
    l = np.eye(n)
    r = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i <= j:
                sum = 0
                for k in range(i):
                    sum += l[i][k] * r[k][j]
                r[i][j] = matrix[i][j] - sum
            else:
                sum = 0
                for k in range(i):
                    sum += l[i][k] * r[k][j]
                if r[j][j]==0:
                    raise ZeroDivisionError("не получилось декомпозировать матрицу")
                l[i][j] = (matrix[i][j] - sum) / r[j][j]

    #Проверка на вшивость
    for i in range(n):
        if r[i,i] ==0 or l[i,i]==0:
            raise ValueError("Введенную матрицу невозможно декомпозировать")
    return r, l


def solve_lz(l, b_matrix):
    n = len(l)
    z = np.zeros(n)
    if l[0][0] == 0:
        raise ZeroDivisionError("Исходная матрица вырожденная либо элемент (1,1) равен нулю")
    z[0] = b_matrix[0] / l[0][0]
    for i in range(1, n):
        if l[i][i]==0:
            raise ZeroDivisionError("Исходная матрица вырожденная либо элемент (1,1) равен нулю")
        z[i] = (b_matrix[i] - np.dot(l[i][:i], z[:i])) / l[i][i]
        if abs(z[i])< 10**(-10):
            z[i] = 0
    return z


def solve_x(r, z): #rz = x
    n = len(r)
    x = np.zeros(n)
    if r[-1][-1] == 0:
        raise ZeroDivisionError("Исходная матрица вырожденная либо элемент (1,1) равен нулю")
    x[-1] = z[-1]/r[-1][-1]
    for i in range(2, n+1):
        j = n - i
        if r[j][j]==0:
            raise ZeroDivisionError("Исходная матрица вырожденная либо элемент (1,1) равен нулю")
        x[j] = (z[j] - np.dot(r[j, j:n], x[j:n])) / r[j][j]
        if abs(x[j])< 10**(-10):
            x[j] = 0
    return x


def solver(matrix, b):
    r, l = lu_decomp(matrix)
    z = solve_lz(l, b)
    x = solve_x(r, z)
    return x
