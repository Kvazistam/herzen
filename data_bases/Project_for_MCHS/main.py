# from App.App import start_app
#
# start_app()
import math

summ = 0
for i in range(20, 1000):
    max_x = 1 / 4 * (4 * math.pi * i + math.pi)
    min_x = 1 / 4 * (4 * math.pi * i - math.pi)
    if 200 >= max_x >= 100:
        summ += max_x
    if 200 >= min_x >= 100:
        summ += min_x
print(summ)