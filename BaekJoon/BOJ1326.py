from sys import stdin
from collections import deque

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
src,des = map(int,stdin.readline().split())

visit = [-1]*N
visit[src-1] = 0
queue = deque()
queue.append(src-1)
ans = -1
while queue:
    cur = queue.popleft()
    if cur == des-1:
        ans = visit[cur]
        break

    for i in range(cur,N,nums[cur]):
        if visit[i] == -1:
            queue.append(i)
            visit[i] = visit[cur]+1

    for i in range(cur,-1,-nums[cur]):
        if visit[i] == -1:
            queue.append(i)
            visit[i] = visit[cur]+1

print(ans)
