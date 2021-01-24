n,w=map(int,input().split())

item =[]
value = []

for i in range(n):
    temp_i,temp_v = map(int,input().split())
    item.append(temp_i)
    value.append(temp_v)

dp= [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        if item[i-1] <= j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-item[i-1]]+value[i-1])
        else:
            dp[i][j] = dp[i-1][j]
