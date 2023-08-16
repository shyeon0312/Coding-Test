# 1953 (재귀함수) 삼각형 출력하기 1

def print_tri(n, k):
    if k <= n:
        temp = '*' * k
        print(temp)
        print_tri(n, k + 1)

n = int(input())
print_tri(n, 1)