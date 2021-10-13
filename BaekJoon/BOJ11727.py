from sys import stdin

N = int(stdin.readline())

dp = [0]*(N+1)
dp[1]=1
if N>1:
    dp[2]=3

for i in range(3,N+1):
    dp[i] = (dp[i-1]+2*dp[i-2])%10007

print(dp[-1])
