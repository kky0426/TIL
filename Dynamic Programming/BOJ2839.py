kg=int(input())
dp=list(range(0,kg+1))


for i in range(kg+1):
    if i<=5:
        if i==3 or i==5:
            dp[i]=1
        else:
            dp[i]=9999
    else:
        if dp[i-3]==9999 and dp[i-5]==9999:
            dp[i]=9999
        else:
            dp[i]=min(dp[i-3],dp[i-5])+1

if dp[kg]==9999:
    print(-1)
else:
    print(dp[kg])
