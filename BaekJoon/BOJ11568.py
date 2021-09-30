from sys import stdin
import bisect

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [nums[0]]
for i in range(1,N):
    if dp[-1]<nums[i]:
        dp.append(nums[i])
    else:
        idx = bisect.bisect_left(dp,nums[i])
        dp[idx] = nums[i]

print(len(dp))
