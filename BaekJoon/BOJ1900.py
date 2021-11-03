from sys import stdin

N = int(stdin.readline())

player = [tuple(map(int,stdin.readline().split())) for _ in range(N)]

win = [0]*N

for i in range(N):
    for j in range(i+1,N):
        if player[i][0]+player[i][1]*player[j][0]>player[j][0]+player[j][1]*player[i][0]:
            win[i]+=1
        else:
            win[j]+=1

ans = []
for i in range(N):
    ans.append((win[i],i+1))
ans.sort(reverse=True)

for _,i in ans:
    print(i)
