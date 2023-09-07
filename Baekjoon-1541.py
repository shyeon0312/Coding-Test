# 1541 잃어버린 괄호
import sys

input = sys.stdin.readline
text = input().split('-')
nbrs = []
for x in text:
    y = list(map(int, x.split('+')))
    temp = 0
    for nbr in y:
        temp += nbr
    nbrs.append(temp)
print(nbrs[0]-sum(nbrs[1:]))