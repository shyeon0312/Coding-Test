# 4751 아시아 정보올림피아드
import heapq

n = int(input())
scores = {}
for _ in range(n):
    a, b, c = map(int, input().split())
    scores[c] = [a, b]

scores = sorted(scores.items())

nation = [0] * 101
cnt = 0
while cnt < 3:
    x = scores.pop()
    if nation[x[1][0]] < 2:
        print(x[1][0], x[1][1])
        nation[x[1][0]] += 1; cnt += 1