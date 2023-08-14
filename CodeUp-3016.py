# 3016 1등한 학생의 성적
n = int(input())
name = []; s1 = []; s2 = []; s3 = []
for i in range(n):
    a, b, c, d = input().split()
    name.append(a)
    s1.append(int(b)); s2.append(int(c)); s3.append(int(d))

k = s1.index(max(s1))

r2 = sorted(s2, reverse=True)
r3 = sorted(s3, reverse=True)

print(name[k], r2.index(s2[k])+1, r3.index(s3[k])+1)