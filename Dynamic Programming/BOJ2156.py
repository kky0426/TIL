n=int(input())

wine = []
dp=[0]*(n+1)

for i in range(n):
    wine.append(int(input()))



for i in range(0,n):
    if i<2:
        dp[i+1]=dp[i]+wine[i]
    else:
        dp[i+1] = max(dp[i-1],dp[i-2]+wine[i-1]) + wine[i]
        dp[i+1] = max(dp)

print(dp[-1])
