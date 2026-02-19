# Данный код является реализацией лекционной задачи по проверке гипотез
import math
from scipy.special import ndtr, erf
import scipy.stats as stats


def laplas(x):
    return stats.norm.cdf(x) - 0.5


def first_task():
    concrete_table = [[(190, 200), 195, 10], [(200, 210), 205, 26], [(210, 220), 215, 56], [(220, 230), 225, 64],
                      [(230, 240), 235, 30], [(240, 250), 245, 14]]
    significance_level = 0.001
    l = len(concrete_table)
    summ = 0
    freedom_degree = l-2-1
    for i in range(l):
        summ += concrete_table[i][2]

    n = summ
    summ = 0
    for i in range(l):
        summ += concrete_table[i][1] * concrete_table[i][2]
    average_x = summ / n
    print(f'Задача 1. Среднее значение интервала= {average_x}')

    summ = 0
    for i in range(l):
        summ += (((concrete_table[i][1]) - average_x) ** 2) * concrete_table[i][2]
    expected_value = math.sqrt(summ / n)
    print(f'Задача 1. Матиматическое ожидание= {expected_value}')

    list_u = [(concrete_table[i][0][0] - average_x) / expected_value for i in range(l)]
    list_u[0] = -math.inf
    list_u.append(math.inf)
    print(f'Задача 1. Столбец 3= {list_u}')
    list_p = [laplas(list_u[i]) - laplas(list_u[i + 1]) for i in range(len(list_u) - 1)]
    print(f'Задача 1. Столбец 4= {list_p}')
    list_np = [abs(round(n * list_p[i], 1)) for i in range(l)]
    print(f'Задача 1. Столбец 5= {list_np}')
    list_nnp = [round((concrete_table[i][2] - list_np[i]) ** 2, 2) for i in range(l)]
    print(f'Задача 1. Столбец 6= {list_nnp}')
    list_ksi = [list_nnp[i] / list_np[i] for i in range(l)]
    print(f'Задача 1. Столбец 7= {list_ksi}')
    ksi = sum(list_ksi)
    print(f'Задача 1. Статистика Пирсона = {ksi}')
    teor_ksi = stats.chi2.ppf(1-significance_level, freedom_degree)
    print(f'Задача 1. Теоритическая Статистика Пирсона = {teor_ksi}')
    if teor_ksi>ksi:
        print("Гипотеза верна")
    else:
        print("Гипотеза не доказана")
first_task()
