# 12891 DNA 비밀번호
import sys

input = sys.stdin.readline
S, P = map(int, input().split())
dna = input()
A, C, G, T= map(int, input().split())

global dna_cnt, check
dna_cnt = [0] * 4
check = False

def add2(x):
    global dna_cnt, check
    if x == 'A': dna_cnt[0] += 1
    elif x == 'C': dna_cnt[1] += 1
    elif x == 'G': dna_cnt[2] += 1
    elif x == 'T': dna_cnt[3] += 1

    check = (dna_cnt[0] >= A) and (dna_cnt[1] >= C) and (dna_cnt[2] >= G) and (dna_cnt[3] >= T)
    return

def pop2(x):
    global dna_cnt
    if x == 'A': dna_cnt[0] -= 1
    elif x == 'C': dna_cnt[1] -= 1
    elif x == 'G': dna_cnt[2] -= 1
    elif x == 'T': dna_cnt[3] -= 1
    return

head = 0; tail = P; ans = 0
while(tail <= S):
    if head == 0:
        for x in dna[head:tail]:
            add2(x)
    else:
        pop2(dna[head - 1])
        add2(dna[tail - 1])
    if check: ans += 1
    head += 1; tail += 1
print(ans)


