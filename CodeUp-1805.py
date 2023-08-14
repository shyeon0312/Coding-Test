# 1805 입체기동장치 생산공장
import sys

n = int(input())
data = {}
for i in range(n):
    d = list(map(int, input().split()))
    data[d[0]] = d[1]

for d in sorted(data.items()):
    print(d[0], d[1])
