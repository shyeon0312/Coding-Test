# 17298 오큰수
import sys

input = sys.stdin.readline
n = int(input())
nbrs = list(map(int, input().split()))
check = [-1] * n
mystack = []

for i in range(n):
    if len(mystack) == 0:
        mystack.append(i)
    else:
        while mystack:
            if nbrs[i] > nbrs[mystack[-1]]:
                idx = mystack.pop()
                check[idx] = nbrs[i]
            else:
                break
        mystack.append(i)
    
print(*check, sep=' ')