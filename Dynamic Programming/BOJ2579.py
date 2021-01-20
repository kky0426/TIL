n=int(input())

dp=[0]*(n+1)
stairs=[]
for i in range(n):
    stairs.append(int(input()))

dp[1]=stairs[0]


for i in range(2,n+1):
    dp[i]=max(dp[i-2]+stairs[i-1],dp[i-3]+stairs[i-2]+stairs[i-1])

print(dp[n])
