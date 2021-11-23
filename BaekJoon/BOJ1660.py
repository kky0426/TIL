from sys import stdin
N = int(stdin.readline())

num = [0]*(151)

for i in range(1,151):
    num[i] = num[i-1]+i

for i in range(1,150):
    num[i+1]+=num[i]

dp = [float("inf")]*(N+1)
dp[0]=0
for i in range(1,N+1):
    j=1
    while num[j]<=i:
        dp[i] = min(dp[i],dp[i-num[j]]+1)
        j+=1

print(dp[-1])
