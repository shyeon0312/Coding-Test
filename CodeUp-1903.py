# 1903 SuperSum

import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
from sys import stdin

def SuperSum(k, n):
    global mat_ss
    if k == 0:
        mat_ss[k][n] = n
        return n
    else:
        temp = 0
        for i in range(1, n + 1):
            if mat_ss[k-1][i] == 0:
                mat_ss[k-1][i] = SuperSum(k - 1, i)
            temp += mat_ss[k-1][i]
        mat_ss[k][n] = temp
        return mat_ss[k][n]

global mat_ss
mat_ss = np.zeros([15, 15])

for line in stdin:
    if line != '':
        k, n = map(int, line.split(' '))
        print(int(SuperSum(k, n)))