from sys import stdin
import sys
sys.setrecursionlimit(1000000)
def find(x):
    if x==parent[x]:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x]=y
    cost = min(money[x],money[y])
    money[x]=cost
    money[y]=cost

N,M,K = map(int,stdin.readline().split())
parent = [x for x in range(N+1)]
money = list(map(int,stdin.readline().split()))
money.insert(0,0)


for _ in range(M):
    u,v = map(int,stdin.readline().split())
    union(u,v)

ans=0

visit = set()
for i in range(1,N+1):
    x = find(i)
    if not x in visit:
        visit.add(x)
        ans+=money[x]

if ans<=K:
    print(ans)
else:
    print("Oh no")
