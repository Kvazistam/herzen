from for_lab_8 import MNK, data_func
import numpy as np

if __name__ == '__main__':
    print("введите степень многочлена")
    degree = int(input())
    degree+=1
    file = "data.txt"
    xv, yv = data_func.get_points(file)
    solve = MNK.solver(degree, xv, yv)
    func = MNK.polynom(solve)
    # Вывод функции
    print("Q(x) = " + MNK.print_polynom(solve))

    #График
    data_func.create_graph(xv, yv,func)



    # a = [[5.0, 7.0, 6.0, 5.0], [7.0, 10.0, 8.0, 7.0], [6.0, 8.0,10.0, 9.0], [5.0, 7.0, 9.0, 10.0]]
    # b = [23.1, 31.9, 33.03,31.01]
    # solve = np.linalg.solve(a, b)
    # print(solve)
