import numpy as np

import triangle_fact.kvadrat_koren
import triangle_fact.LU_decomposition



a = np.array([[0,0,0,0], [7,10,8,7], [6,8,10,9],[5,7,9,10]])
b=np.array([23,32,33,31])

c=np.array([[1,2,3],
            [2,7,5],
            [3,5,11]])
d=np.array([1,12,31])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(triangle_fact.LU_decomposition.solver(a, b))
    print(triangle_fact.kvadrat_koren.solver(c,d))
