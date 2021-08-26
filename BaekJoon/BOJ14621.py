from sys import stdin


def find(x):
    if x==parent[x]:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y


N,M = map(int,stdin.readline().split())
gender = list(stdin.readline().split())
parent = [n for n in range(N)]
graph = []

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph.append((u-1,v-1,w))
graph.sort(key=lambda x:x[2])

ans = 0
connect = 0
for u,v,w in graph:
    if find(u)!=find(v) and gender[u]!=gender[v]:
        union(u,v)
        ans+=w
        connect+=1

print(ans if connect==N-1 else -1)
