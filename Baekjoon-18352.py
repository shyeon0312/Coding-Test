# 18352 특정 거리의 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N + 1)

def BFS(v):
    global visited
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)

BFS(X)
for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer: print(-1)
else:
    answer.sort()
    print(*answer, sep='\n')

