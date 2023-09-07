# 1931 회의실 배정
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
A = [[0] * 2 for _ in range(n)]

for i in range(n):
    start, end = map(int, input().split())
    A[i][0] = end
    A[i][1] = start
A.sort()
print(A)
cnt = 0; end = -1
for i in range(n):
    if A[i][1] >= end:
        end = A[i][0]
        cnt += 1
print(cnt)