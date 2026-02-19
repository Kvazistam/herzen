from tkinter import messagebox

import matplotlib.pyplot as plt
from tkinter import *
from scipy.special import erf

alf = {}
alf2 = {}

start = 1
stop = 2
step = 0.1

values = [float(i) / 10 for i in range(int(start * 10), int((stop + step) * 10), int(step * 10))]


def getPoints(file):
    q = open(file, 'r')
    n = 0
    arrayOfPoints = []
    try:
        for i in q:
            arrayOfPoints.append((i.split()))

            alf2[(arrayOfPoints[n][0])] = (arrayOfPoints[n][1])
            arrayOfPoints[n][0] = float(arrayOfPoints[n][0])
            arrayOfPoints[n][1] = float(arrayOfPoints[n][1])
            n += 1
    except IndexError:
        q.close()
        raise ValueError

    q.close()
    return arrayOfPoints


def addPoints(func, values):
    fp = open("data.txt", 'w')
    for i in values:
        fp.write(str(i) + " " + str(func(i)) + '\n')
    fp.close()


# xv- массив иксов, yv-массив y
def razd(xv, yv, k):
    sum = 0
    for i in range(k + 1):
        pr = 1
        for j in range(k + 1):
            if j != i:
                pr *= (xv[i] - xv[j])
        sum = sum + (yv[i]) / pr
    return sum


def final_difference(yv, i, deg):
    if alf.get((i, deg)) is not None:
        return alf[(i, deg)]
    if (deg == 1):
        res = yv[i] - yv[i - 1]
        alf[(i, deg)] = res
        return res
    else:
        return final_difference(yv, i, deg - 1) - final_difference(yv, i - 1, deg - 1)


def newton(xv, yv, m):
    # arrayOfPoints = getPoints()
    # arr = []
    # arr1=[]
    # sum = fun(arrayOfPoints[0][0])
    rep = []
    ravn = True
    h = xv[1] - xv[0]
    for i in range(1, len(xv)):
        if xv[i] - xv[i - 1] != h:
            ravn = False
            break
    if not ravn:
        for i in range(1, len(xv)):
            rep.append((razd(xv, yv, i)))

    else:
        for i in range(1, len(xv)):
            rep.append(final_difference(yv, i, i))

    def new1(x):
        result = yv[0]
        for k in range(1, m + 1):
            pr = 1
            for j in range(k):
                pr *= (x - xv[j])
            result += rep[k - 1] * pr
        return result

    def new2(x):
        res = yv[0]
        q = x - xv[0] / h
        for k in range(1, m + 1):
            q = q * (q - k + 1) / k
            res = res + q * rep[k - 1]
        return res

    if ravn:
        print(new2(1.43))
        return new2

    else:
        return new1


def bnt_click():
    plt.style.use('seaborn-v0_8-whitegrid')
    try:
        # b = int(loginOfb.get())
        # a = int(loginOfa.get())
        # n = int(loginOfn.get())
        a = values[0]
        b = values[-1]
        m = int(loginOfm.get())
        xss = float(loginOfa.get())
    except ValueError:
        messagebox.showerror(title='Ошибка типа данных', message='введите данные корректно')
        return
    # if (b - a <= 0 or n <= 0 or m > n or m <= 0):
    #     messagebox.showerror(title='Некорректно введены данные', message='введите данные корректно')
    #     return

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    try:
        addPoints(erf, values)
        xv = [getPoints()[i][0] for i in range(len(getPoints()))]
        yv = [getPoints()[i][1] for i in range(len(getPoints()))]
    except ValueError:
        messagebox.showerror(title='Некорректно введены данные', message='введите данные корректно')
        return
    yn = []
    yl = []
    x1 = []
    for i in range(1001):
        x1.append(a + (b - a) * i / 1000)
    try:
        newpol = newton(xv, yv, m)
        for i in x1:
            yn.append(newpol(i))

        ax1.plot(x1, yn)
        ax1.plot(xv, yv)
        loginOftext.config(text=str(newpol(xss)))

        plt.show()
    except ValueError:
        messagebox.showerror(title='Некорректно введены данные', message='введите данные корректно1')

    return


import numpy as np


def divided_differences(x, y, degree):
    n = degree + 1
    coefficients = np.zeros(n)
    for j in range(n):
        coefficients[j] = y[j]
        for i in range(j - 1, -1, -1):
            coefficients[i] = (coefficients[i + 1] - coefficients[i]) / (x[j] - x[i])
    return coefficients


def newton_polynomial(coefficients, xv):
    n = len(coefficients)
    result = ''
    for i in range(n):
        term = coefficients[i]
        if i == 0:
            result += f"{term:.6f}"
        else:
            result += f"{'+' if term > 0 else ''}{term:.2f}"

        for j in range(i):
            result += f"*(x{' - ' if xv[i] > 0 else ' + '}{abs(xv[j]):.2f})"
    return result


def bnt2():
    try:
        m = int(loginOfm.get())
        xss = float(loginOfa.get())
        if str(login_of_data.get()) == "":
            file = "data.txt"
        else:
            file = str(login_of_data.get())

        if m <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(title='Некорректно введены данные', message='введите степень многочлена корректно')
        return
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    try:
        mylist = getPoints(file)
        mylist.sort(key=lambda x: x[0])
        xv = [mylist[i][0] for i in range(len(mylist))]
        yv = [mylist[i][1] for i in range(len(mylist))]
        if len(xv) < m:
            raise ValueError
    except ValueError:
        messagebox.showerror(title='Некорректно введены данные', message='введите данные корректно')
        return
    yn = []
    yl = []
    coef = divided_differences(xv, yv, m)

    try:
        newpol = newton(xv, yv, m)
        for i in xv:
            yn.append(newpol(i))

        ax1.plot(xv, yn)
        ax1.plot(xv, yv)
        loginOftext.config(text=str(newpol(xss)))
        title_func.config(text=str("f(x) =" + newton_polynomial(coef, xv)))

        plt.show()
    except ValueError:
        messagebox.showerror(title='Некорректно введены данные', message='введите данные корректно1')
        return
    except ZeroDivisionError:
        messagebox.showerror(title='абциссы двух точек совпадают', message='введите данные корректно1')

    return


root = Tk()
root.title('lab 2')
root.geometry('400x400')
frame = Frame(root, bg='grey')
frame.place(relheight=1, relwidth=1)
title_func = Label(frame, text='Многочлен ньютона', bg='gray', width=200)

# title3 = Label(frame, text="количество точек, n=", bg='gray')
# loginOfn = Entry(frame, bg='white', )
title4 = Label(frame, text="Cтепень многочлена, m=", bg='gray')
loginOfm = Entry(frame, bg='white', )
title5 = Label(frame, text="Введите название файла, в котором лежат точки.", bg='gray')
login_of_data = Entry(frame, bg='white', )
title2 = Label(frame, text='Посчитать значение полинома в точке ', bg='gray')
loginOfa = Entry(frame, bg='white', )
loginOftext = Label(frame, text="Значение функции=", bg='gray')

# lang.pack(side=LEFT)
# new.pack(side=LEFT)
# title.pack()
title2.pack()
loginOfa.pack()

# loginOfb.pack()
# title3.pack()
# loginOfn.pack()
title4.pack()
loginOfm.pack()
title5.pack()
login_of_data.pack()
bnt = Button(frame, text='Построить график', bg='gray', command=bnt_click)
button2 = Button(frame, text='Построить график по заданным точкам', bg='gray', command=bnt2)
bnt.pack()
button2.pack()
loginOftext.pack()
title_func.pack()
root.mainloop()
