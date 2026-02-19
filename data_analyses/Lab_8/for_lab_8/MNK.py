import numpy as np


def s_calc(degree, xv):
    res = 0
    if degree == 0:
        return len(xv)
    for i in xv:
        res += i ** degree
    return res


def t_calc(degree, xv, yv):
    res = 0
    for i in range(len(yv)):
        res += yv[i] * xv[i] ** degree
    return res


def solver(degree, xv, yv):
    matrix = np.zeros((degree, degree))
    v_free = np.zeros((degree, 1))
    for i in range(degree):
        v_free[i][0] = t_calc(i, xv, yv)
        for j in range(degree):
            matrix[i][j] = s_calc(i + j, xv)
    solve = np.linalg.solve(matrix, v_free)
    return solve.flatten()


def polynom(solve):
    def func(x):
        res = 0
        for i in range(len(solve)):
            res += solve[i] * x ** i
        return res

    return func


def print_polynom(solve):
    res = ""
    for i in range(len(solve)):
        res += f"{'+' if solve[i] > 0 else ''}{solve[i]:.3f}{ '*x^' if i>0 else ''}{i if i>0 else ''}"
    return res

