from sys import stdin
from collections import deque

A,B,C = map(int,stdin.readline().split())

x,y = 0,0

ans = []
visit = [[False for _ in range(B+1)] for _ in range(A+1)]
def insertQ(x,y):
    if not visit[x][y]:
        queue.append((x,y))
        visit[x][y]=True

queue =deque()
def bfs():
    queue.append((0,0))
    visit[0][0] = True

    while queue:
        x,y = queue.popleft()
        z = C - x - y
        if x == 0:
            ans.append(z)

        #A->B
        move = min(x,B-y)
        insertQ(x-move,y+move)
        #A->C
        move = min(x,C-z)
        insertQ(x-move,y)
        #B->A
        move = min(y,A-x)
        insertQ(x+move,y-move)
        #B->C
        move = min(y,C-z)
        insertQ(x,y-move)
        #C->A
        move = min(z,A-x)
        insertQ(x+move,y)
        #C->B
        move = min(z,B-y)
        insertQ(x,y+move)

bfs()
ans.sort()
print(" ".join(map(str,ans)))
