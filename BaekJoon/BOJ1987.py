from sys import stdin
import sys
sys.setrecursionlimit(10**6)


R,C = map(int,stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = []
for _ in range(R):
    board.append(stdin.readline())

def bfs(x,y):
    queue = set()
    count = 0
    queue.add((x,y,1,board[x][y]))

    while queue:
        x,y,dis,word = queue.pop()
        count = max(count,dis)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] not in word:
                queue.add((nx,ny,dis+1,word+board[nx][ny]))
    return count

print(bfs(0,0))
