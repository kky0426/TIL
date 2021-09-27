from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [float("inf")]*N

dp[0] = 0
for i in range(N):
    for j in range(i+1,i+nums[i]+1):
        if j>=N:
            continue
        dp[j] = min(dp[j],dp[i]+1)

print(dp[-1] if dp[-1]!=float("inf") else -1
