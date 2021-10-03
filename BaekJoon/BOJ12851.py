from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

count = 0

visit = [-1]*100001
queue = deque()
queue.append(N)
visit[N]=0

while queue:
    cur = queue.popleft()
    if cur == K:
        count+=1
        continue

    for next in [cur-1,cur+1,cur*2]:
        if 0<=next<100001:
            if visit[next] == -1 or visit[next]==visit[cur]+1:
                queue.append(next)
                visit[next]=visit[cur]+1

print(visit[K])
print(count)
