from sys import stdin
from collections import deque
from itertools import combinations
import copy

N,M,D = map(int,stdin.readline().split())
dx = [0,-1,0]
dy = [-1,0,1]

board = [list(map(int,stdin.readline().split())) for _ in range(N)] + [[0]*M]

def bfs(x,y,board):
    visit = set()
    queue = deque()
    queue.append((x,y,0))
    visit.add((x,y))
    temp = []
    while queue:
        x,y,dis = queue.popleft()
        if dis>D: break
        if board[x][y] == 1:
            temp.append((x,y,dis))
            continue
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N+1 and 0<=ny<M and (nx,ny) not in visit:
                queue.append((nx,ny,dis+1))
                visit.add((nx,ny))
    temp.sort(key=lambda x:(x[2],x[1]))
    if temp:
        return temp[0]
    else:
        return -1,-1,-1






def move(board):
    return [[0]*M] + board[:N-1]+[[0]*M]


idx = [i for i in range(M)]
ans = 0
for candidate in combinations(idx,3):
    count=0
    temp = copy.deepcopy(board)

    for _ in range(N):
        death=[]
        for y in candidate:
            nx,ny,_ = bfs(N,y,temp)
            if nx==-1 and ny==-1:
                continue
            death.append((nx,ny))
        death = set(death)
        count += len(death)
        for x,y in death:
            temp[x][y] = 0

        temp = move(temp)
    ans = max(ans,count)
print(ans)
