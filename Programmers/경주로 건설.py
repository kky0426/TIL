from collections import deque

def solution(board):
    answer = 10000000
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    N = len(board) 
    def bfs(x,y,direction):
        queue=deque()
        queue.append((x,y,0,-1))
        board[x][y] = 1
        while queue:
            x,y,cost,direction = queue.popleft()
            if x==N-1 and y==N-1:
                nonlocal answer
                answer = min(answer,cost)
                
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N and board[nx][ny]!=1:
                    if direction==-1 or direction==i:
                        n_cost=cost+100
                    else:
                        n_cost=cost+600
                    
                    if board[nx][ny] == 0 or board[nx][ny]>=n_cost:
                        board[nx][ny] = n_cost
                        queue.append((nx,ny,n_cost,i))
                    
    bfs(0,0,-1)
    return answer
