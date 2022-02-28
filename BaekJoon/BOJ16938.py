from sys import stdin

N,L,R,X = map(int,stdin.readline().split())

problems = list(map(int,stdin.readline().split()))
ans = 0
visit = [False]*(N+1)
def solve(idx,count,mx,mi,s):
    if count == 0:
        if L<=s<=R and X<=mx-mi:
            global ans
            ans+=1
        return

    for i in range(idx,N):
        if not visit[i]:
            visit[i]=True
            solve(i,count-1,max(mx,problems[i]),min(mi,problems[i]),s+problems[i])
            visit[i]=False

for n in range(2,N+1):
    solve(0,n,0,float("inf"),0)

print(ans)

