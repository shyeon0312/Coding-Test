# 2164 카드2
import sys
import math

input = sys.stdin.readline
n = int(input())
x = int(math.log2(n))
if n <= 2:
    print(n)
elif n == (2 ** x):
    print(n)
else:
    print((n - 2 ** x) * 2)
