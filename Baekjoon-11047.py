# 11047 동전 0
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0
for c in reversed(coins):
    cnt += k // c
    k = k % c

print(cnt)