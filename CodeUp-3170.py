# 3170 기억력 테스트 09

n, m = map(int, input().split())
data = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if data.get(s) is None:
        data[s] = k
    else:
        data[s] = k + data[s]

for _ in range(m):
    q = input()
    if data.get(q) is None:
        print(0)
    else:
        print(data[q])