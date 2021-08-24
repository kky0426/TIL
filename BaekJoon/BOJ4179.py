from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
dx =[1,-1,0,0]
dy =[0,0,1,-1]

board = [list(stdin.readline().rstrip()) for _ in range(N)]

fire = deque()
person = deque()

def bfs(fire,person):
    f_visit = [[0 for _ in range(M)] for _ in range(N)]
    p_visit = [[0 for _ in range(M)] for _ in range(N)]
    for x,y in fire:
        f_visit[x][y]=1

    for x,y in person:
        p_visit[x][y]=1

    while fire:
        x,y = fire.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not f_visit[nx][ny] and board[nx][ny]!='#':
                f_visit[nx][ny] = f_visit[x][y]+1
                fire.append((nx,ny))

    while person:
        x,y = person.popleft()
        if x==0 or x==N-1 or y==0 or y==M-1:
            return p_visit[x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and not p_visit[nx][ny] and board[nx][ny]!='#':
                if f_visit[nx][ny]==0 or f_visit[nx][ny]>p_visit[x][y]+1:
                    p_visit[nx][ny] = p_visit[x][y]+1
                    person.append((nx,ny))

    return "IMPOSSIBLE"

for i in range(N):
    for j in range(M):
        if board[i][j] == "F":
            fire.append((i,j))
        elif board[i][j] == "J":
            person.append((i,j))

print(bfs(fire,person))
