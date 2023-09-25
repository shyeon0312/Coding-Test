# 1456 거의 소수
import sys, math

input = sys.stdin.readline
a, b = map(int, input().split())

A = list(range(10000001))
A[1] = 0
for i in range(2, int(math.sqrt(len(A))) + 1):
    if A[i] == 0: continue
    for j in range(i + i, len(A), i):
        A[j] = 0

cnt = 0
for i in range(2, len(A)):
    if A[i] != 0:
        temp = A[i] * A[i]
        while temp <= b:
            if temp >= a:
                cnt += 1
            temp *= A[i]
print(cnt)