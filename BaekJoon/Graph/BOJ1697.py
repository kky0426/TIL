import sys
from collections import deque

N,K=map(int,sys.stdin.readline().rstrip().split())
queue = deque()
visit=[0]*100001
queue.append((N,0))

while queue:
    pos,count=queue.popleft()
    visit[pos]=1
    if pos == K:
        print(count)
        break

    if  0<=pos-1<=100000 and visit[pos-1] ==0:
        queue.append((pos-1,count+1))
        visit[pos-1]=1
    if 0<=pos+1<=100000 and visit[pos+1] ==0:
        queue.append((pos+1,count+1))
        visit[pos + 1] = 1
    if 0<=pos*2<=100000 and visit[pos*2] ==0:
        queue.append((pos*2,count+1))
        visit[pos * 2] = 1
