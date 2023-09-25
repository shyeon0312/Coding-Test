# 2251 물통
import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
ans = [False] * (c + 1)
ans[c] = True
if a <= c:
    ans[c - a] = True
    ans[a] = True
if b <= c:
    ans[c - b] = True
    ans[b] = True

for i in range(c + 1):
    if ans[i]: print(i, end = ' ')