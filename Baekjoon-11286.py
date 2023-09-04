# 11286 절댓값 힙
import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
heap = []
ans = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            ans.append(0)
        else:
            ans.append(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))

print(*ans, sep='\n')
