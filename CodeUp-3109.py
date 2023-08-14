# 3109 정올 참여 학생 리스트 만들기 2
from collections import deque

n = int(input())
data = {}
for i in range(n):
    c, a, b = input().split()
    a = int(a)
    if c == 'I':
        if data.get(a) is None:
            dq = deque()
            dq.append(b)
            data[a] = dq
        else:
            data[a].append(b)
    
    if c == 'D':
        if data.get(a) is not None:
            data[a].pop()
            
data = dict(sorted(data.items()))
items = [str(key)+' '+data[key].pop() for key in data.keys() for _ in range(len(data[key]))]

idx = input().split()
for i in idx:
    print(items[int(i) - 1])