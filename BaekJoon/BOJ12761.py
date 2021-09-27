from sys import stdin
from collections import deque

A,B,N,M = map(int,stdin.readline().split())
visit = [False]*100001

def bfs(start):
    visit[start]=True
    queue = deque()
    queue.append((start,0))
    while queue:
        cur,count = queue.popleft()
        if cur == M:
            return count

        if cur+1<=100000 and not visit[cur+1]:
            visit[cur+1]=True
            queue.append((cur+1,count+1))
        if 0<=cur-1 and not visit[cur-1]:
            visit[cur-1]=True
            queue.append((cur-1,count+1))

        if cur+A<=100000 and not visit[cur+A]:
            visit[cur+A] = True
            queue.append((cur+A,count+1))

        if 0<=cur-A and not visit[cur-A]:
            visit[cur-A] = True
            queue.append((cur-A,count+1))

        if cur+B<=100000 and not visit[cur+B]:
            visit[cur+B] = True
            queue.append((cur+B,count+1))

        if 0<=cur-B and not visit[cur-B]:
            visit[cur-B] = True
            queue.append((cur-B,count+1))

        if cur*A<=100000 and not visit[cur*A]:
            visit[cur*A] = True
            queue.append((cur*A,count+1))

        if cur*B<=100000 and not visit[cur*B]:
            visit[cur*B] = True
            queue.append((cur*B,count+1))

print(bfs(N))
