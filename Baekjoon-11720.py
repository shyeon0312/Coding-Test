# 11720 숫자의 합 구하기

n = int(input())
nbrs = input()
sum = 0
for i in range(n):
    sum += int(nbrs[i])

print(sum)