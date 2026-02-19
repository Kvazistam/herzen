import math
from scipy.stats import norm, t, chi2


def task_1(dispersion=9, n=9, x_cp=48, a=49, p=0.95):
    hypothesis_1 = False
    t = (x_cp - a) * math.sqrt(n) / math.sqrt(dispersion)
    t_cr = norm.ppf(p)  # Обратная функция лапласа
    if abs(t) <= t_cr:
        hypothesis_1 = True
    if hypothesis_1:
        return "a=" + str(a)
    else:
        return "a!=" + str(a)


print("Верна гипотеза " + task_1())


def task_2(lambd=0.05, hyp_1=187500, x_cp=175000, n=10, s=35000):
    alpha = 1 - lambd / 2
    statistic = (x_cp - hyp_1) * math.sqrt(n) / s
    t_cr = t.ppf(alpha, n - 1)
    if abs(statistic) <= t_cr:
        return "а = " + str(hyp_1)
    else:
        return "a != " + str(hyp_1)


print("Верна гипотеза " + task_2())

def task_3(lamd=0.1,hyp_s=0.25,disp=0.15,n=25):
    u=0
    alpha = 1 - lamd
    t_cr = chi2.ppf(1 - alpha, n-1)
    statistic = (n-1)*hyp_s/disp
    if abs(statistic)<=t_cr:
        return "s2= " + str(hyp_s)
    else:
        return "s2 !=" + str(hyp_s)
print("Верна гипотеза " + task_3())

def task_4(xi=None, yi=None, lambd=0.1, ):
    if yi is None:
        yi = [(303, 2), (304, 6), (306, 4), (308, 1)]
    if xi is None:
        xi = [(304, 1), (307, 4), (308, 4)]
    nx=0
    ny=0
    x_cp=0
    for i in xi:
        x_cp+=i[0]*i[1]
        nx+=i[1]
    x_cp=x_cp/nx
    y_cp=0
    for i in yi:
        y_cp+=i[0]*i[1]
        ny+=i[1]
    y_cp=y_cp/ny
    s2=0
    s1 = 0
    for i in xi:
        s1+=(i[0]-x_cp)**2
    s1=s1/(nx)
    for i in yi:
        s2 += (i[0] - y_cp) ** 2
    s2 = s2 / (ny)
    statistic = (x_cp-y_cp)/math.sqrt((nx*s1+ny*s2)/(nx+ny-2)*(1/nx+1/ny))
    alpha=1-lambd/2
    t_cr=t.ppf(alpha, nx+ny-2)
    if abs(statistic)<=t_cr:
        return "Гипотеза о равенстве средних верна"
    else:
        return "Гипотеза о равенстве средних неверна"
print(task_4())