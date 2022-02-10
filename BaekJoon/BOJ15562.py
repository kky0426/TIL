from sys import stdin

N,M = map(int,stdin.readline().split())

in_degree = [0]*N
out_dgree = [0]*N

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    in_degree[u-1]+=1
    out_dgree[v-1]+=1

ans = 0
for i in range(N):
    ans+=max(out_dgree[i]-in_degree[i],0)

print(ans)
