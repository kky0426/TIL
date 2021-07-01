from sys import stdin
from collections import deque
test = int(input())

for _ in range(test):
    M,N,K = map(int,stdin.readline().split())
    board = [[0 for _ in range(N)] for _ in range(M)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    for _ in range(K):
        i,j = map(int,stdin.readline().split())
        board[i][j] = 1

    def bfs(i,j):
        queue.append((i,j))
        board[i][j] = 0
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<M and 0<=ny<N and board[nx][ny] == 1:
                    queue.append((nx,ny))
                    board[nx][ny] = 0
    ans = 0

    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                bfs(i,j)
                ans+=1
    print(ans)
