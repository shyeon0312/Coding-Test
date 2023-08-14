# 3108 정올 참여 학생 리스트 만들기 1

n = int(input())
data = {}
for i in range(n):
    c, a, b = input().split()
    a = int(a)
    if c == 'I':
        if data.get(a) is None:
            data[a] = b
    elif c == 'D':
        if data.get(a) is not None:
            data.pop(a)
idx = list(map(int, input().split()))

data_s = list(sorted(data.items()))
for i in idx:
    print(*data_s[i-1])