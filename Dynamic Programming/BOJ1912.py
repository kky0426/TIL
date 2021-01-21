n = int(input())

num = list(map(int,input().split()))

dp=[0]*(n+1)
dp[0]=-1001
for i in range(1,n+1):
    if i<2:
        dp[i]=num[i-1]
    else:
        dp[i] = max(dp[i-1]+num[i-1],num[i-1])

print(max(dp))
