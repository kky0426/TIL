from sys import stdin
import copy
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,stdin.readline().split())
board=[list(map(int,stdin.readline().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 0<board[i][j]<6:
            cctv.append((board[i][j],i,j))

head = [(1,0),(0,1),(-1,0),(0,-1)]

direction_list = [[],[[0],[1],[2],[3]],
                  [[0,2],[1,3]],
                  [[0,1],[1,2],[2,3],[3,0]],
                  [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
                  [[0,1,2,3]]]
ans = float("inf")

def dfs(board,cctv,check):
    if check == len(cctv):
        global ans
        count = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    count+=1
        ans = min(ans,count)
        return

    num,x,y = cctv[check]
    for direction in direction_list[num]:
        temp = copy.deepcopy(board)
        for dir in direction:
            nx = x+head[dir][0]
            ny = y+head[dir][1]
            while 0<=nx<N and 0<=ny<M:
                if temp[nx][ny] == 6:
                    break
                elif temp[nx][ny] == 0:
                    temp[nx][ny]=-1
                nx+=head[dir][0]
                ny+=head[dir][1]
        dfs(temp,cctv,check+1)

dfs(board,cctv,0)
print(ans)
