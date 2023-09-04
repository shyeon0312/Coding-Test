# 1427 소트인사이드
import sys

input = sys.stdin.readline
n = input()
nbrs = []
for x in n[:-1]:
    nbrs.append(int(x))

def selection_sort(x):
    for i in range(len(x)):
        changed = False
        maxnum = i
        for j in range(i, len(x)):
            if x[maxnum] < x[j]:
                maxnum = j
                changed = True
        if changed:
            temp = x[i]
            x[i] = x[maxnum]
            x[maxnum] = temp
    return x

x = selection_sort(nbrs)
print(*x, sep='')