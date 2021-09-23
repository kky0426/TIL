from sys import stdin

N,M = map(int,stdin.readline().split())

parent = [i for i in range(N)]

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y



ans = 0
for i in range(1,M+1):
    u,v = map(int,stdin.readline().split())
    if find(u) == find(v):
        ans = i
        break
    union(u,v)

print(ans)
