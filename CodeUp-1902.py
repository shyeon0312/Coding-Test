# 1902 (재귀함수) 1부터 n까지 역순으로 출력하기

def print_until_n(k):
    if k > 0:
        print(k)
        print_until_n(k-1)

n = int(input())
print_until_n(n)