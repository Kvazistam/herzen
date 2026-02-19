import math

import numpy as np


def lu_sim_decomp(matrix):
    n = len(matrix)
    r = np.zeros((n, n))
    r[0][0]=math.sqrt(matrix[0][0])
    for i in range(n):
        for j in range(i+1):
            if matrix[i][j] != matrix[j][i]:
                raise ValueError("Матрица не симметричная " + str(matrix[i][j]) + " " + str(matrix[j][i]))
    for i in range(1,n):
        r[0][i] = matrix[0][i]/r[0][0]

    for i in range(n):
        sum = 0
        for k in range(i):
            sum += r[k][i] ** 2
        r[i][i] = math.sqrt(matrix[i][i] - sum)
        if r[i][i]==0:
            raise ZeroDivisionError("Матрицу невозможно декомпозировать")
        for j in range(i+1, n):
            sum=0
            for k in range(i):
                sum+=r[k][i]*r[k][j]
            r[i][j] = (matrix[i][j] - sum)/r[i][i]
    l = r.transpose()
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
    r, l = lu_sim_decomp(matrix)
    z = solve_lz(l, b)
    x = solve_x(r, z)
    return x
