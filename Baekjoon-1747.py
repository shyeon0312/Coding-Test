# 1747 소수&팰린드롬
import sys, math

input = sys.stdin.readline

global A, max_nbr
n = int(input())
max_nbr = 10000001
A = list(range(max_nbr))
A[1] = 0

# 소수 구하기
def get_decimal():
    global A, max_nbr
    for i in range(2, int(math.sqrt(max_nbr)) + 1):
        if A[i] == 0: continue
        for j in range(i+i, max_nbr, i):
            A[j] = 0

def is_palindromic(x):
    s1 = str(x)
    s2 = str(x)[::-1]
    for i in range(len(s1)//2):
        if s1[i] != s2[i]:
            return False
    return True

# 최소 팰린드롬 확인
get_decimal()
for i in range(n, max_nbr):
    if A[i] != 0:
        if is_palindromic(A[i]):
            print(A[i])
            break