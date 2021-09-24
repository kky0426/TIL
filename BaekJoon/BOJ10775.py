from sys import stdin

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

G = int(stdin.readline())
P = int(stdin.readline())
parent = [i for i in range(G+1)]
air = [int(stdin.readline()) for _ in range(P)]
ans = 0
for i in air:
    x = find(i)
    if x == 0:
        break
    union(x,x-1)
    ans+=1
print(ans)
