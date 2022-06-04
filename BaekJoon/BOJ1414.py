from sys import stdin
import heapq

N = int(stdin.readline())

graph = [list(stdin.readline().rstrip()) for _ in range(N)]
queue = []
parent = [i for i in range(N)]
def convert(ch):
    if ch.islower():
        return ord(ch)-ord("a")+1
    else:
        return ord(ch)-ord("A")+27

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

ans = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == "0":
            continue
        w = convert(graph[i][j])
        heapq.heappush(queue,(w,i,j))
        ans+=w

connect = 0
while queue and connect<N:
    w,u,v = heapq.heappop(queue)
    if find(u)!=find(v):
        union(u,v)
        ans-=w
        connect+=1

print(ans if connect == N-1 else -1)