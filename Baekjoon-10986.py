# 10986 나머지 합
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nbrs = list(map(int, input().split()))

pre_sum = [0] * n
remain = [0] * m
for i in range(n):
    if i == 0:
        pre_sum[i] = nbrs[i] % m
    else:
        pre_sum[i] = (pre_sum[i-1] + nbrs[i]) % m
    remain[pre_sum[i]] += 1

ans = 0
for i in range(m):
    x = remain[i]
    if i == 0:
        ans += remain[i]
    if x > 1:
        ans += x * (x - 1) // 2
print(ans)
