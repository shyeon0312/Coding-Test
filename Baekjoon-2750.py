# 2750 수 정렬하기
import sys

n = int(input())
num_list = []

for _ in range(n):
    x = int(input())
    num_list.append(x)

# print(num_list)
num_list = sorted(num_list)
for i in num_list:
    print(i)