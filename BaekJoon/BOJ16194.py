from sys import stdin

N = int(stdin.readline())

price = list(map(int,stdin.readline().split()))
M = len(price)
dp = [float("inf")]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j]+price[j-1])

print(dp[-1])
