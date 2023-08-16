# 1904 (재귀함수) 두 수 사이의 홀수 출력하기

def print_odd(b, k):
    if k <= b:
        if (k % 2) != 0:
            print(k)
        print_odd(b, k + 1)

a, b = map(int, input().split())
print_odd(b, a)
