# 13023 ABCDE
import sys
from heapq import *

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def make_start_point(cnt):
    start = []; temp = []
    for i in range(n):
        heappush(start, (cnt[i], i))
    for _ in range(n):
        x = heappop(start)
        temp.append(x[1])
    return temp

def dfs(v, i):
    global visited, A, ans
    if i == 5:
        ans = 1
        return
    else:
        visited[v] = True
        for x in A[v]:
            if not visited[x]:
                dfs(x, i+1)
    visited[v] = False

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b); cnt[a] += 1
    A[b].append(a); cnt[b] += 1

start = make_start_point(cnt)
ans = 0
for i in start:
    dfs(i, 1)
    if ans: break
print(ans)