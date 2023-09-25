# 1929 소수 구하기
import sys, math

input = sys.stdin.readline
m, n = map(int, input().split())

A = list(range(n + 1))
A[1] = 0

for i in range(2, int(math.sqrt(n)) + 1): # 제곱근까지
    if A[i] == 0:
        continue
    for j in range(i + i, n + 1, i):
        A[j] = 0

for i in range(m, n+1):
    if A[i] != 0: print(A[i])