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
parent=[x for x in range(N+1)]
truth = list(map(int,stdin.readline().split()))[1:]

party=[]
for _ in range(M):
    invited = list(map(int,stdin.readline().split()))[1:]
    party.append(invited)
    for i in range(len(invited)-1):
        for j in range(i+1,len(invited)):
            union(invited[i],invited[j])

s=set()
for t in truth:
    s.add(find(t))
ans=0
for p in party:
    flag=True
    for i in p:
        if find(i) in s:
            flag=False
            break
    if flag:
        ans+=1
print(ans)
