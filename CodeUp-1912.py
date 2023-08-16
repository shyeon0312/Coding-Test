# 1912 (재귀함수) 팩토리얼 계산

def factorial(k, m):
    if k > 1:
        m *= k
        factorial(k - 1, m)
    elif k == 1:
        m *= k
        print(m)
        

n = int(input())
factorial(n, 1)