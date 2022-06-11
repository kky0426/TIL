from sys import stdin
import heapq

N,M = map(int,stdin.readline().split())

queue =[]
ans = 0

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    heapq.heappush(queue,(w,u,v))
    ans+=w
parent = [i for i in range(N+1)]

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

connect = 0
while queue:
    w,u,v = heapq.heappop(queue)
    if find(u)!=find(v):
        union(u,v)
        ans-=w
        connect+=1

    if connect == N-1:
        break

print(ans if connect==N-1 else -1)