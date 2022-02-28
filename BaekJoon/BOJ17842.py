from sys import stdin

N = int(stdin.readline())
degree = [0]*(N+1)
for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    degree[u]+=1
    degree[v]+=1

leaf = 0
for n in degree:
    if n == 1:
        leaf+=1

print(leaf//2+leaf%2)
