from sys import stdin
from collections import deque

N = int(stdin.readline())

visit = [[-1 for _ in range(N+1)] for _ in range(N+1)]
visit[1][0] = 0

queue = deque()
queue.append((1,0))
while queue:
    count,clip = queue.popleft()
    if count == N:
        print(visit[count][clip])
        break

    if visit[count][count] == -1:
        visit[count][count] = visit[count][clip]+1
        queue.append((count,count))

    if visit[count-1][clip] == -1 and 0<=count-1:
        visit[count-1][clip] = visit[count][clip]+1
        queue.append((count-1,clip))

    if count+clip<=N and visit[count+clip][clip] == -1:
        visit[count+clip][clip] = visit[count][clip]+1
        queue.append((count+clip,clip))
