# 2023 신기한 소수
import sys

input = sys.stdin.readline
n = int(input())
global arr; arr = []

def is_decimal(x):
    if x == 1: return False
    for i in range(2, (x//2) + 1):
        if (x % i) == 0: return False
    return True

def make_decimal(x, n):
    global arr
    if len(str(x)) == n:
        arr.append(x)
    else:
        for i in [1, 3, 7, 9]:
            nbr = int(str(x)+str(i))
            if is_decimal(nbr):
                make_decimal(nbr, n)

for i in [2, 3, 5, 7]:
    make_decimal(i, n)
print(*arr, sep='\n')

        