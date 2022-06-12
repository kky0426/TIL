from sys import stdin
import heapq
N = int(stdin.readline())

parent = [i for i in range(N)]

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

ans = []
C = 0
M = 0
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]
queue = []
for i in range(N):
    for j in range(i+1,N):
        if graph[i][j] < 0:
            union(i,j)
            C-=graph[i][j]
        else:
            heapq.heappush(queue,(graph[i][j],i,j))

while queue:
    w,u,v = heapq.heappop(queue)
    if find(u)!=find(v):
        union(u,v)
        M+=1
        C+=w
        ans.append((u,v))
print(C,M)
for u,v in ans:
    print(u+1,v+1)