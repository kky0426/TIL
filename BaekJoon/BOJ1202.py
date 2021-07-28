from sys import stdin
import heapq
from collections import deque
N,K=map(int,stdin.readline().split())
ans=0
jewelry=[]
queue=[]
bags=[]
for _ in range(N):
    w,v = map(int,stdin.readline().split())
    jewelry.append((w,v))

for _ in range(K):
    bags.append(int(stdin.readline()))

bags.sort()
jewelry.sort(key=lambda x:x[0])
jewelry=deque(jewelry)
for bag in bags:
    while jewelry and bag>=jewelry[0][0]:
        heapq.heappush(queue,-jewelry[0][1])
        jewelry.popleft()

    if queue:
        ans+=heapq.heappop(queue)
    elif not jewelry:
        break

print(-ans)
