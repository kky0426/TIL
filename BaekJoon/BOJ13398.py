from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))

dp=[[-float("inf") for _ in range(2)] for _ in range(N+1)]


for i in range(1,N+1):
    dp[i][0] = max(dp[i-1][0]+nums[i-1],nums[i-1])

for i in range(1,N+1):
    dp[i][1] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])

ans = -float("inf")
for num in dp:
    ans = max(ans,max(num))
print(ans)
