from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())

place = [list(map(int,stdin.readline().split())) for _ in range(N+1)]

dp = [[-1 for _ in range(5)] for _ in range(100001)]
dx = [0,0,1,-1,0]
dy = [1,-1,0,0,0]

def get_dis(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def move(x,y,idx,dir):
    if idx == N:
        return 0
    dis = dp[idx][dir]
    if dis!=-1:
        return dis
    dis = float("inf")
    for i in range(5):
        nx = place[idx+1][0]+dx[i]
        ny = place[idx+1][1]+dy[i]
        dis = min(dis,move(nx,ny,idx+1,i)+get_dis(x,y,nx,ny))
    dp[idx][dir] = dis
    return dis

print(move(place[0][0],place[0][1],0,0))


