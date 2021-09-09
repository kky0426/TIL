from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

visit = [0]*200001
path = [0]*200001
def bfs():
    visit[N] = True
    queue=deque()
    queue.append((N,0))
    while queue:
        cur,time = queue.popleft()
        if cur == K:
            print(time)
            ans=[]
            while cur!=N:
                ans.append(cur)
                cur = path[cur]
            ans.append(N)
            ans.reverse()
            print(" ".join(map(str,ans)))
            return
        for next in (cur+1,cur-1,cur*2):
            if 0<=next<200001 and not visit[next]:
                visit[next]=True
                path[next] = cur
                queue.append((next,time+1))

bfs()

