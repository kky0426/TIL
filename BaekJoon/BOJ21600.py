from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    if nums[i-1]>dp[i-1]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = nums[i-1]


print(max(dp))