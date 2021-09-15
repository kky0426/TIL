from sys import stdin
from collections import deque

F,S,G,U,D = map(int,stdin.readline().split())

queue = deque()
queue.append((S,0))
visit = [False]*(F+1)
visit[S] = True
ans = -1
while queue:
    floor,count = queue.popleft()
    if floor == G:
        ans = count
        break
    if 0<floor+U<=F and not visit[floor+U]:
        queue.append((floor+U,count+1))
        visit[floor+U]=True

    if 0<floor-D<=F and not visit[floor-D]:
        queue.append((floor-D,count+1))
        visit[floor-D] = True

if ans>-1:
    print(ans)
else:
    print("use the stairs")
