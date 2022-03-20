from sys import stdin

T = int(stdin.readline())

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return temp

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        size[x]+=size[y]



for _ in range(T):
    parent = {}
    size = {}
    N = int(stdin.readline())
    for _ in range(N):
        u, v = stdin.readline().split()
        if not u in parent:
            parent[u] = u
            size[u] = 1
        if not v in parent:
            parent[v] = v
            size[v] = 1

        union(u,v)
        print(size[find(u)])

