# 2343 기타 레슨
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
runtime = list(map(int, input().split()))

start = 0; end = 0
for x in runtime:
    if x > start : start = x
    end += x

while start <= end:
    mid = (start + end) // 2
    sum = 0; cnt = 0
    for x in runtime:
        if sum + x > mid:
            cnt += 1; sum = 0
        sum += x
    if sum != 0: cnt += 1

    if cnt > m: start = mid + 1
    else : end = mid - 1
           
print(start)
