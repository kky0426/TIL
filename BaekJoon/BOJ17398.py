from sys import stdin


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if count[x]<count[y]:
        parent[x] = y
        count[y]+=count[x]
        count[x]=count[y]
    else:
        parent[y] = x
        count[x]+=count[y]
        count[y] = count[x]

N,M,Q = map(int,stdin.readline().split())

connect = [True]*(M+1)

edges = [list(map(int,stdin.readline().split())) for _ in range(M)]
parent = [i for i in range(N+1)]

count = [1]*(N+1)

rm_edges = []
for _ in range(Q):
    r = int(stdin.readline())
    rm_edges.append(r)
    connect[r] = False

for i in range(1,M+1):
    if connect[i]:
        union(edges[i-1][0],edges[i-1][1])

ans = 0
while rm_edges:
    node_num = rm_edges.pop()
    u,v = edges[node_num-1]
    x = find(u)
    y = find(v)
    if x!=y:
        ans+=count[x]*count[y]
    union(x,y)

print(ans)