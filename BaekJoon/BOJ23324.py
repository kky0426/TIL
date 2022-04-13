from sys import stdin


N,M,K = map(int,stdin.readline().split())
parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x]  = temp
        return temp

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(1,M+1):
    u,v = map(int,stdin.readline().split())
    if i == K:
        continue
    union(u,v)

left = 0
right = 0
for i in range(1,N+1):
    if i == find(i):
        if left == 0:
            left = i
        else:
            right = i

if left!=0 and right!=0:
    print(parent.count(find(left))*parent.count(find(right)))
else:
    print(0)