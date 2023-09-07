# 1715 카드 정렬하기
import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
cards = []
for _ in range(n):
    heappush(cards, int(input()))

data1 = 0; data2 = 0; total = 0
while len(cards) > 1:
    data1 = heappop(cards)
    data2 = heappop(cards)
    total += data1 + data2
    heappush(cards, data1 + data2)
print(total)