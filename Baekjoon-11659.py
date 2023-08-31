# 11659 구간 합 구하기 4
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nbrs = list(map(int, input().split()))

nbrs = [0] + nbrs
pre_sum = [0] * (n + 1)

for i in range(1, n + 1):
    pre_sum[i] = pre_sum[i-1] + nbrs[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(pre_sum[b] - pre_sum[a-1])