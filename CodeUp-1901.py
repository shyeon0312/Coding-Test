# 1901 (재귀함수) 1부터 n까지 출력하기

def print_until_n(k, n):
    if k <= n:
        print(k)
        print_until_n(k+1, n)

n = int(input())
print_until_n(1, n)