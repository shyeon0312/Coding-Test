# 1934 최소공배수
import sys

def gcd(x, y):
    a, b = x, y
    while a != 0 and b != 0:
        if a >= b: a = a % b
        else:      b = b % a
    if a == 0: return int( x * y / b)
    else:      return int( x * y / a)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(gcd(x, y))