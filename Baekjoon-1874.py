# 1874 스택 수열
import sys

input = sys.stdin.readline
n = int(input())
nbrs = []
mystack = [0]
check = 1; is_possible = True
cal = []

for _ in range(n):
    x = int(input())
    nbrs.append(x)

for x in nbrs:
    # push
    if (x > mystack[-1]):
        while(check <= x):
            mystack.append(check)
            cal.append('+')
            check += 1
    # pop
    while (x > mystack[-1]):
        mystack.pop()
        cal.append('-')
        if mystack is None:
            break
    if x == mystack[-1]:
        mystack.pop()
        cal.append('-')
    else:
        is_possible = False

if is_possible:
    print(*cal, sep='\n')
else:
    print('NO')
    
    