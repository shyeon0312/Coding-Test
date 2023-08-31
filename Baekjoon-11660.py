# 11660 구간 합 구하기 5
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nbrs = []
nbrs.append([0] * (n + 1))
for _ in range(n):
    row = list(map(int, input().split()))
    nbrs.append([0] + row)

pre_sum = [ [0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        pre_sum[i][j] = nbrs[i][j] + pre_sum[i][j-1] + pre_sum[i-1][j] - pre_sum[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = pre_sum[x2][y2] - pre_sum[x2][y1-1] - pre_sum[x1-1][y2] + pre_sum[x1-1][y1-1]
    print(sum)