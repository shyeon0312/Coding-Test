# 3702 파스칼의 삼각형 2
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np

def pascals_tri(r, c):
    global tri
    if (r == 1) or (c == 1):
        tri[r][c] == 1
        return 1
    else:
        if tri[r - 1][c] == 0:
            tri[r - 1][c] = pascals_tri(r - 1, c)
        if tri[r][c - 1] == 0:
            tri[r][c - 1] = pascals_tri(r, c - 1)
        tri[r][c] = tri[r - 1][c] + tri[r][c - 1]
        return tri[r][c] % 100000000

global tri
tri = np.zeros([51, 51])
r, c = map(int, input().split())
print(int(pascals_tri(r, c) % 100000000))

        