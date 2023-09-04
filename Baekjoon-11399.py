# 11399 ATM
import sys

input = sys.stdin.readline
n = int(input())
nbrs = list(map(int, input().split()))
nbrs = sorted(nbrs)

times = [nbrs[0]]
sum = times[0]
for i in range(1, n):
    times.append(times[i-1] + nbrs[i])
    sum += times[i]
print(sum)