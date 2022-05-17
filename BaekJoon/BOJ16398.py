from sys import stdin
import heapq

N = int(stdin.readline())

graph = [list(map(int,stdin.readline().split())) for _ in range(N)]
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

queue = []
for i in range(N-1):
    for j in range(i+1,N):
        heapq.heappush(queue,(graph[i][j],i,j))

ans = 0
count = 0

while queue:
    cost,u,v = heapq.heappop(queue)
    if find(u)!=find(v):
        union(u,v)
        ans+=cost
        count+=1

    if count == N-1:
        break

print(ans)