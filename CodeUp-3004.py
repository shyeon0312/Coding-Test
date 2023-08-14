# 3004 데이터 재정렬
import sys

n = int(input())
data = list(map(int, input().split()))


s_data = sorted(data)

rank = {s_data[i]:i for i in range(n)}
for d in data:
    print(rank[d], end=' ')