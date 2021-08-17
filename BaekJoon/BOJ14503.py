from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,stdin.readline().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

row,col,direction = map(int,stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int,stdin.readline().split())))
ans = 0

def cleaning(x,y,d):
    if board[x][y] == 0:
        board[x][y] = 2
        global ans
        ans+=1

    for _ in range(4):
        nd=(d+3)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if board[nx][ny] == 0:
            cleaning(nx,ny,nd)
            return
        d = nd

    nd = (d+2)%4
    nx = x+dx[nd]
    ny = y+dy[nd]
    if board[nx][ny] == 1:
        return
    cleaning(nx,ny,d)

cleaning(row,col,direction)
print(ans)
