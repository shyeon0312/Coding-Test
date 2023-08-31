# 1940 주몽의 명령
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
nbrs = list(map(int, input().split()))

# ans = 0
# check = [0] * 10000000
# cnt_nbrs = [0] * 10000000
# for i in nbrs:
#     cnt_nbrs[i] += 1

# for x in nbrs:
#     check[x] += 1
#     if (check[m - x] == 0) and (cnt_nbrs[m - x] > 0):
#         ans += cnt_nbrs[m - x]

# print(ans)

nbrs = sorted(nbrs)
head = 0; tail = n - 1; ans = 0
while head < tail:
    sum = nbrs[head] + nbrs[tail]
    if sum < m: head += 1
    elif sum > m: tail -= 1
    else: ans += 1; head += 1; tail -= 1
print(ans)