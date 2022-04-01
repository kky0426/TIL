from sys import stdin
from collections import deque

N,S,D,F,B,K = map(int,stdin.readline().split())

police = set(map(int,stdin.readline().split()))

ans = float("inf")
queue = deque()
queue.append((S,0))
visit = [False]*(N+1)
while queue:
    cur,dis = queue.popleft()
    if cur == D:
        ans = min(ans,dis)
        break

    if cur-B>0 and not visit[cur-B] and cur-B not in police:
        queue.append((cur-B,dis+1))
        visit[cur-B] = True
    if cur+F<=N and not visit[cur+F] and cur+F not in police:
        queue.append((cur+F,dis+1))
        visit[cur+F] = True

print(ans if ans!=float("inf") else "BUG FOUND")