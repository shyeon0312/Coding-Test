# 1517 버블 소트

n = int(input())
global nbrs, cnt
nbrs = list(map(int, input().split()))
cnt = 0

def cnt_swap(start, end):
    global nbrs, cnt
    mid = (start + end) // 2
    pt1 = start; pt2 = mid + 1
    if (start != mid) and (end != mid):
        cnt_swap(start, mid)
        cnt_swap(mid + 1, end)

    temp = []; k = start
    while (pt1 <= mid) and (pt2 <= end):
        if nbrs[pt1] <= nbrs[pt2]:
            temp.append(nbrs[pt1])
            pt1 += 1; k += 1
        else:
            temp.append(nbrs[pt2])
            cnt += pt2 - k
            pt2 += 1; k += 1
    while (pt1 <= mid):
        temp.append(nbrs[pt1])
        pt1 += 1; k += 1
    while (pt2 <= end):
        temp.append(nbrs[pt2])
        pt2 += 1; k += 1
    nbrs[start : end + 1] = temp
    return

cnt_swap(0, n - 1)
print(cnt)