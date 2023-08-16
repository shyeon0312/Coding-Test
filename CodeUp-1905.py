# 1905 (재귀함수) 1부터 n까지 합 구하기

import sys
sys.setrecursionlimit(10**5)
def sum_until_n(n, k, s):
    if (k < n):
        s += k
        sum_until_n(n, k + 1, s)
    elif k == n:
        s += k
        print(s)

n = int(input())
sum_until_n(n, 1, 0)