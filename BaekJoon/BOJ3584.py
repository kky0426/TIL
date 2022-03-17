from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    parent = [i for i in range(N+1)]
    for _ in range(N-1):
        p,c = map(int,stdin.readline().split())
        parent[c] = p
    u,v = map(int,stdin.readline().split())
    visit = [False]*(N+1)
    visit[u] = True
    while u!=parent[u]:
        u = parent[u]
        visit[u] = True

    while True:
        if visit[v]:
            print(v)
            break
        else:
            v = parent[v]

