# 1920 수 찾기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def binary_search(arr, x):
    start = 0; end = len(arr) - 1
    while (start >= 0) and (end < len(arr)) and (start <= end):
        mid = (start + end) // 2
        if x == arr[mid]: print(1); return
        elif x < arr[mid]: end = mid - 1
        else: start = mid + 1
    print(0); return
    
n = int(input())
nbrs = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

nbrs.sort()
for x in find:
    binary_search(nbrs, x)
