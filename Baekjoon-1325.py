# 1325 효율적인 해킹
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
trust = [0] * (N + 1)
def BFS(v):
    global A, visited, trust
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                trust[i] += 1
                queue.append(i)

for _ in range(M):
    s, e= map(int, input().split())
    A[s].append(e)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    BFS(i)

maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, trust[i])

for i in range(1, N + 1):
    if maxVal == trust[i]:
        print(i, end = ' ')