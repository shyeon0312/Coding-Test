# 3015 성적표 출력
n, m = map(int, input().split())
name = []; score = []
for i in range(n):
    x, y = input().split()
    name.append(x); score.append(int(y))

rank = {i:score[i] for i in range(n)}
rank = dict(sorted(rank.items(), key=lambda item:item[1], reverse=True))

for i in list(rank.keys())[:m]:
    print(name[i])