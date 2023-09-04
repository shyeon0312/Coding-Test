# 2751 수 정렬하기 2
import sys

input = sys.stdin.readline
n = int(input())
global nbrs
nbrs = []
for _ in range(n):
    nbrs.append(int(input()))

def merge_sort(start, end):
    global nbrs
    mid = (start + end) // 2
    pt1 = start; pt2 = mid + 1
    # merging
    if (start < end - 1) and (mid != end):
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
    
    # sorting
    sorted_arr = []
    while (pt1 <= mid) and (pt2 <= end):
        if nbrs[pt1] <= nbrs[pt2]:
            sorted_arr.append(nbrs[pt1])
            pt1 += 1
        else:
            sorted_arr.append(nbrs[pt2])
            pt2 += 1
    while (pt1 <= mid):
        sorted_arr.append(nbrs[pt1])
        pt1 += 1
    while (pt2 <= end):
        sorted_arr.append(nbrs[pt2])
        pt2 += 2
    nbrs[start:end+1] = sorted_arr
    return

merge_sort(0, n-1)
print(*nbrs, sep='\n')