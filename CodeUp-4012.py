# 4012 석차 계산

n = int(input())
scores = list(map(int, input().split()))

cnt = [0] * 101
for i in scores:
    cnt[i] += 1

for i in scores:
    rank = sum(cnt[i+1:]) + 1
    print(i, rank)