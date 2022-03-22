from sys import stdin


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
    if x>y:
        parent[x] = y
    elif x<y:
        parent[y] = x

T = int(stdin.readline())

for t in range(1,T+1):
    N = int(stdin.readline())
    parent = [i for i in range(N+1)]
    K = int(stdin.readline())
    for _ in range(K):
        u,v = map(int,stdin.readline().split())
        union(u,v)
    M = int(stdin.readline())
    print("Scenario {}:".format(t))
    for _ in range(M):
        u,v = map(int,stdin.readline().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()