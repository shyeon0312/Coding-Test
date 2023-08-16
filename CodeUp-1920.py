# 1920 (재귀함수) 2진수 변환

def to_binary(n, k):
    quotient = k // 2
    remainder = k % 2
    if n < 2:
        print(n)
    if quotient > 1:
        to_binary(n, quotient)
        print(remainder, end='')
    elif quotient == 1:
        print(quotient, end='')
        print(remainder, end='')

n = int(input())
to_binary(n, n)