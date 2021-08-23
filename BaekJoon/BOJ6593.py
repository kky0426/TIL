from sys import stdin
from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while True:
    H,R,C = map(int,stdin.readline().split())
    if H==0 and R==0 and C==0:
        break
    board = []
    
    for _ in range(H):
        temp = []
        for _ in range(R):
            temp.append(list(stdin.readline()))
        board.append(temp)
        stdin.readline()
    
    def bfs(x,y,z):
        visit = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]
        visit[z][x][y] = True
        queue = deque()
        queue.append((x,y,z,0))
        ans = float("inf")
        while queue:
            x,y,z,count= queue.popleft()
            if board[z][x][y] == "E":
                ans = min(ans,count)
                return ans
            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                nz=z+dz[i]
    
                if 0<=nx<R and 0<=ny<C and 0<=nz<H:
                    if not visit[nz][nx][ny]:
                        if board[nz][nx][ny]!="#":
                            queue.append((nx,ny,nz,count+1))
                            visit[nz][nx][ny]=True
    
        return ans
    
    
    for x in range(R):
        for y in range(C):
            for z in range(H):
                if board[z][x][y] == "S":
                    ans = bfs(x,y,z)
                    print("Escaped in {} minute(s).".format(ans) if ans!=float("inf") else "Trapped!")
