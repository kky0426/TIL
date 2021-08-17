from sys import stdin
from itertools import combinations


N,M = map(int,stdin.readline().split())
chicken = []
board =[]
for i in range(N):
    line = list(map(int,stdin.readline().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 2:
            chicken.append((i,j))


candidates = list(combinations(chicken,M))
ans = float("inf")


for candidate in candidates:
    distance=0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                dis = float("inf")
                for x,y in candidate:
                    dis = min(dis,abs(i-x)+abs(j-y))
                distance+=dis
    ans = min(ans,distance)
print(ans)
