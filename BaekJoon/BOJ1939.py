from sys import stdin
from collections import defaultdict
from collections import deque

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)

maxW=0
for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
    maxW=max(maxW,w)

start,end = map(int,stdin.readline().split())

def bfs(weight):
    visit=[False]*(N+1)
    queue = deque()
    queue.append((0,start))
    while queue:
        _,node = queue.popleft()
        if node == end: return True
        for w,n in graph[node]:
            if visit[n]==False and w>=weight:
                queue.append((w,n))
                visit[n]=True
    return False

ans=0
left=0
right = maxW

while left<=right:
    mid = left+(right-left)//2
    if bfs(mid):
        ans=mid
        left=mid+1
    else:
        right=mid-1

print(ans)
