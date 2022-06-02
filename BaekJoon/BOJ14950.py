from sys import stdin
import heapq

N,M,t = map(int,stdin.readline().split())
parent = [i for i in range(N+1)]
queue = []

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    heapq.heappush(queue,(w,u,v))

count = 0
ans = 0
while queue:
    w,u,v = heapq.heappop(queue)
    if find(u) != find(v):
        union(u,v)
        ans+=count*t + w
        count+=1
    if count == N-1:
        break

print(ans)
