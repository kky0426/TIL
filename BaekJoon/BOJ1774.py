from sys import stdin
import heapq
import math

N,M = map(int,stdin.readline().split())

spot = [list(map(int,stdin.readline().split())) for _ in range(N)]

parent = [i for i in range(N)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x]=y

def get_dis(node1,node2):
    return math.sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    union(u-1,v-1)


queue = []

for i in range(N-1):
    for j in range(i+1,N):
        dis = get_dis(spot[i],spot[j])
        heapq.heappush(queue,(dis,i,j))

ans = 0
while queue:
    dis,u,v = heapq.heappop(queue)
    if find(u)!=find(v):
        ans+=dis
        union(u,v)
        M+=1
    if M==N-1:
        break


print("%0.2f"%ans)
