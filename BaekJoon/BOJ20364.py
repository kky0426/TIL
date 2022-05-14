from sys import stdin

N,Q = map(int,stdin.readline().split())

visit = [False]*(N+1)

def solve(idx,last):
    parent = idx//2
    if parent == 0:
        print(last)
        return
    if visit[parent]:
        last = parent
    solve(parent,last)

for _ in range(Q):
    n = int(stdin.readline())
    if visit[n]:
        solve(n,n)
    else:
        visit[n] = True
        solve(n,0)
