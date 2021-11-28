from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
dp = [0]*(N+1)

for i in range(N):
    max_num = nums[i]
    min_num = nums[i]
    for j in range(i,-1,-1):
        min_num = min(min_num,nums[j])
        max_num = max(max_num,nums[j])
        dp[i+1] = max(dp[i+1],dp[j]+(max_num-min_num))

print(dp[-1])
