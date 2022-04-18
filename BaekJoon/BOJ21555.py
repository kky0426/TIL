from sys import stdin

N,K = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

dp = [[0 for _ in range(2)] for _ in range(N+1)]

dp[1][0] = A[0]
dp[1][1] = B[0]

for i in range(2,N+1):
    dp[i][0] = min(dp[i-1][0],dp[i-1][1]+K) + A[i-1]
    dp[i][1] = min(dp[i-1][0]+K,dp[i-1][1]) + B[i-1]

print(min(dp[N]))