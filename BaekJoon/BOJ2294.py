from sys import stdin

N,K = map(int,stdin.readline().split())
INF=float('INF')
coins=[]
for _ in range(N):
    coins.append(int(stdin.readline()))

dp=[INF]*(K+1)
dp[0]=0
for i in range(1,K+1):
    for coin in coins:
        if i>=coin and dp[i-coin]!=INF:
            dp[i]=min(dp[i-coin]+1,dp[i])

if dp[-1]==INF:
    print(-1)
else:
    print(dp[-1])
