n=list(input())
m=list(input())


dp= [[0 for _ in range(len(m)+1)] for _ in range(len(n)+1)]


for i in range(len(n)):
    for j in range(len(m)):
        if(n[i]==m[j]):
            dp[i+1][j+1]=dp[i][j]+1
        elif(dp[i+1][j]>dp[i][j+1]):
            dp[i+1][j+1] = dp[i+1][j]
        else:
            dp[i+1][j+1]= dp[i][j+1]

print(dp[-1][-1])
