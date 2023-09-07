# 1744 수 묶기
import sys

input = sys.stdin.readline
n = int(input())

zeros = 0; totalsum = 0
minus = []; plus = []
for _ in range(n):
    x = int(input())
    if x == 0: zeros += 1
    elif x == 1: totalsum += 1
    elif x < 0: minus.append(x)
    else: plus.append(x)

minus = sorted(minus, reverse=True)
plus = sorted(plus)
while minus:
    if len(minus) == 1: break
    totalsum += minus.pop() * minus.pop()
while plus:
    if len(plus) == 1: 
        totalsum += plus.pop(); break
    totalsum += plus.pop() * plus.pop()
if minus and not zeros:
    totalsum += minus.pop()
print(totalsum)