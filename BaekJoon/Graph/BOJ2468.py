from collections import deque
import sys
import copy

N=int(input())
queue=deque()

M=[]
for i in range(N):
    M.append(list(map(int,sys.stdin.readline().split())))
H=max(map(max,M))

def bfs(x,y,mat,queue):
    dx,dy=[1,-1,0,0],[0,0,1,-1]
    queue.append((x,y))
    mat[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and mat[nx][ny]>0:
                mat[nx][ny]=0
                queue.append((nx,ny))

answer=[]
for j in range(H+1):
    copy_M=copy.deepcopy(M)
    queue=deque()
    for k in range(N):
        for h in range(N):
            if copy_M[k][h] <=j:
                copy_M[k][h]=0
    count=0
    for k in range(N):
        for h in range(N):
            if copy_M[k][h]>0:
                count+=1
                bfs(k,h,copy_M,queue)
    answer.append(count)

print(max(answer))
