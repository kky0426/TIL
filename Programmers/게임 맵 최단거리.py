from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visit = [[-1 for _ in range(col)] for _ in range(row)]

    visit[0][0] =1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue = deque()
    queue.append([0,0])
    
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<row and 0<=ny<col and maps[nx][ny] == 1:
                if visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y]+1
                    queue.append([nx,ny])
    return visit[-1][-1]
