# 2178 미로 탐색
import sys
from collections import deque

input = sys.stdin.readline
def BFS(n, m):
    global map, visited
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append((1, 1))
    visited[1][1] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if x == n and y == m:
            break
        for dx, dy in dir:
            now_x = x + dx; now_y = y + dy
            if (now_x >= 0) and (now_y >= 0) and (now_x <= n) and (now_y <= m): # 좌표유효성
                if map[now_x][now_y] and not visited[now_x][now_y]:
                    visited[now_x][now_y] = True
                    queue.append((now_x, now_y))
                    map[now_x][now_y] = map[x][y] + 1

n, m = map(int, input().split())
map = [[0] * (m + 2)]
for _ in range(n):
    x = input()
    temp = []
    for i in range(len(x)-1): 
        temp.append(int(x[i]))
    map.append([0]+temp+[0])
map.append([0] * (m + 2))
visited = [[False] * (m + 2) for _ in range(n + 2)]

BFS(n, m)
print(map[n][m])