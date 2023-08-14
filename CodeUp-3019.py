# 3019 스케줄 정리
n = int(input())
data = []
for i in range(n):
    a, b, c, d = input().split()
    data.append([a, int(b + c + d)])
    
s1 = sorted(data, key=lambda item:item[0])
s2 = sorted(s1, key=lambda item:item[1])

print(*[x[0] for x in s2], sep='\n')