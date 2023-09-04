# 2750 수 정렬하기
import sys

input = sys.stdin.readline
n = int(input())
nbrs = []
for _ in range(n):
    nbrs.append(int(input()))

def bubble_sort(x):
    for i in range(n):
        for j in range(i, n):
            if x[i] > x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

nbrs = bubble_sort(nbrs)
print(*nbrs, sep='\n')