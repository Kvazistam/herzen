import matplotlib.pyplot as plt
import numpy as np


def get_points(file):
    xv = []
    yv =[]
    arr = []
    with open(file, 'r') as fp:
        for line in fp:
            tmp = line.split(' ')
            xv.append(float(tmp[0]))
            yv.append(float(tmp[1]))
            arr.append([float(tmp[0]), float(tmp[1])])
    np_xv = np.array(xv)
    np_yv = np.array(yv)
    sorted_indices = np.argsort(np_xv)
    sorted_xv = np_xv[sorted_indices]
    sorted_yv = np_yv[sorted_indices]

    return sorted_xv, sorted_yv


def create_graph(xv, yv, func, name="Анализ данных", name_x="ocь х", name_y="ось y"):
    fig, axs = plt.subplots()
    fig.suptitle(name)
    axs.set_xlabel(name_x)
    axs.set_ylabel(name_y)
    axs.scatter(xv, yv)
    draw_func(xv, func, axs)
    plt.show()


def draw_func(xv, func, ax):
    yv = []
    for i in xv:
        yv.append(func(i))
    ax.plot(xv, yv)
