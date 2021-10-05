from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

robot = deque([0]*N*2)
belt = deque(list(map(int,stdin.readline().split())))

ans = 1
while True:
    robot.rotate(1)
    belt.rotate(1)
    robot[N-1] = 0

    for i in range(N-2,-1,-1):
        if robot[i]==1 and robot[i+1]==0 and belt[i+1]>0:
            belt[i+1]-=1
            robot[i]=0
            robot[i+1]=1
    robot[N-1] = 0

    if belt[0]>0:
        belt[0]-=1
        robot[0]=1

    if belt.count(0)>=K:
        break
    ans+=1

print(ans)
