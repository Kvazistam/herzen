def is_perfect_square(object n):
    """Проверяет, является ли число полным квадратом."""
    from math import isqrt
    cdef long long root
    root = int(isqrt(n))
    return root * root == n


def fermat_factorization(object N):
    """Разложение числа N на множители методом Ферма."""
    from math import isqrt
    cdef long long y
    cdef object y_squared
    if N % 2 == 0:
        return 2, N // 2  # Если N четное, делим на 2

    x = isqrt(N) + 1  # Начинаем с ближайшего целого числа к √N
    while True:
        y_squared = (x * x) - N
        if is_perfect_square(y_squared):
            y = isqrt(y_squared)
            return (x - y, x + y)  # Возвращаем найденные множители
        x += 1  # Увеличиваем x