# 1370 버블 소트
import sys

input = sys.stdin.readline
n = int(input())
nbrs = []

for i in range(n):
    x = int(input())
    nbrs.append((x, i))

maxswap = 0
nbrs = sorted(nbrs)

for i in range(n):
    if maxswap < (nbrs[i][1] - i):
        maxswap = nbrs[i][1] - i

print(maxswap + 1)