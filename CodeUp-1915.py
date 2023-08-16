# 1915 (재귀함수) 피보나치 수열(Large)

def fibo(n, k, a, b):
    if n < 3:
        print(1)
    else:
        if k == n:
            print(a+b)
        else:
            fibo(n, k + 1, b, a + b)

n = int(input())
fibo(n, 3, 1, 1)