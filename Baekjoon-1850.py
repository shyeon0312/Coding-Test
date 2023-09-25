# 1850 최대공약수
import sys

input = sys.stdin.readline

def gcd(a, b):
    if b == 0: return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
if a >= b : result = gcd(a, b)
else:       result = gcd(b, a)

for _ in range(result): print(1, end='')