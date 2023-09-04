# 1260 DFS와 BFS
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def DFS(now):
    global A, visited
    print(now, end = ' ')
    visited[now] = True
    for v in A[now]:
        if not visited[v]:
            DFS(v)

def BFS(now):
    global A, visited
    queue = deque()
    queue.append(now)
    visited[now] = True

    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for v in A[now]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

n, m, v = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n + 1):
    A[i].sort()

visited = [False] * (n + 1); DFS(v); print()
visited = [False] * (n + 1); BFS(v)