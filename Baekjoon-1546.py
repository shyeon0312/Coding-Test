# 1546 평균 구하기

n = int(input())
score = list(map(int, input().split()))
m = max(score)
print(sum(score) * 100 / (m * n))