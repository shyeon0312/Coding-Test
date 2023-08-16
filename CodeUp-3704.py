# 3704 계단 오르기 2
# import sys
# sys.setrecursionlimit(10**9)

# def n_cases(n):
#     global memo, i
#     if n == 0: memo[0] = 1; return 1
#     if n == 1: memo[1] = 1; return 1
#     if n == 2: memo[2] = 2; return 2
#     if n == 3: memo[3] = 4; return 4
#     if memo[n] != 0: return memo[n]
#     else:
#         memo[n] = n_cases(n - 3) + n_cases(n - 2) + n_cases(n - 1)
#         return (memo[n] % 1000)

# global memo
# n = int(input())
# memo = [0] * (n + 1)
# print(int(n_cases(n)))

n = int(input())
if n == 0: print(1)
elif n == 1: print(1)
elif n == 2: print(2)
elif n == 3: print(4)
else:
    memo = [0] * (n + 1)
    memo[0] = 1; memo[1] = 1; memo[2] = 2; memo[3] = 4
    for i in range(4, n + 1):
        memo[i] = (memo[i - 3] + memo[i - 2] + memo[i - 1]) % 1000
    print(int(memo[n]))