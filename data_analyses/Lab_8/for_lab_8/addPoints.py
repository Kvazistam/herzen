from random import randint


def func(x):
    return 3*x ** 3 - 12 * x ** 2 + randint(-100, 1000)


with open('data.txt', 'w') as f:
    for i in range(18):
        f.write(f'{i} {func(i)}\n')
