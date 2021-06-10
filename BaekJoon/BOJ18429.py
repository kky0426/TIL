from sys import stdin


ans= 0
N,K = map(int,stdin.readline().split())
kit = list(map(int,stdin.readline().rstrip().split()))
visit=[0]*len(kit)

def dfs(count,weight):
    if count == N:
        global ans
        ans+=1
        return
    for i in range(N):
        if visit[i]==0:
            visit[i]=1
            if weight-K+kit[i]>=500:
                dfs(count+1,weight-K+kit[i])
                visit[i]=0
            else:
                visit[i]=0

dfs(0,500)
print(ans)
