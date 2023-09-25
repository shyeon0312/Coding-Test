# 1016 제곱 아닌 수
import sys, math

input = sys.stdin.readline
x, y = map(int, input().split())
root_y = int(math.sqrt(y))
A = [1] * (y - x + 1)
decimals = list(range(root_y + 1))
decimals[1] = 0

# 소수 찾기
for i in range(2, int(math.sqrt(root_y)) + 1):
    if decimals[i] == 0: continue
    for j in range(i + i, root_y + 1, i):
        decimals[j] = 0

# 소수의 배수 없애기
for d in decimals:
    if d == 0: continue
    d2 = d * d
    start = (x // d2) * d2
    end = (y // d2) * d2
    for i in range(start, end + 1, d2):
        if i < x : continue
        A[i - x] = 0
print(sum(A))