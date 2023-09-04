# 11004 K번째 수
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
nbrs = list(map(int, input().split()))

print(sorted(nbrs)[k - 1])