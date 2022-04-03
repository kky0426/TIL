from sys import stdin
import sys
sys.setrecursionlimit(10**5)

N,M = map(int,stdin.readline().split())

parent = [i for i in range(N+1)]


def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return temp


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for _ in range(M):
    command,u,v = map(int,stdin.readline().split())
    if command == 0:
        union(u,v)
    else:
        if find(u) == find(v):
            print("YES")
        else:
            print("NO")

