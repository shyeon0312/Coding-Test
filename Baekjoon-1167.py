# 1167 트리의 지름
import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    global visited, distance
    max_d = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if not visited[now]:
            visited[now] = True
            for v, d in A[now]:
                if not visited[v]:
                    queue.append(v)
                    distance[v] = distance[now] + d
                    max_d = max(max_d, distance[v])
    return max_d
            
n = int(input())
A = [[] for _ in range(n + 1)]
for _ in range(n):
    x = list(map(int, input().split()))
    for i in  range(1, len(x) - 2, 2):
        v, d = x[i], x[i+1]
        A[x[0]].append((v, d))

visited = [False] * (n + 1)
distance = [0] * (n + 1)
BFS(1)
Max = 1
for i in range(2, n + 1):
    if distance[Max] < distance[i]:
        Max = i

visited = [False] * (n + 1)
distance = [0] * (n + 1)
BFS(Max)
print(max(distance))