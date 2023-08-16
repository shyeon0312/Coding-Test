# 1928 (재귀함수) 우박수(3n + 1)
import sys

sys.setrecursionlimit(10**8)
def collatz(n):
    print(n)
    if (n > 1) and (n % 2 == 1): # 홀수이면
        collatz((3 * n) + 1)
    if (n > 1) and (n % 2 == 0): # 짝수이면
        collatz(n//2)

n = int(input())
collatz(n)