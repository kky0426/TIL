from sys import stdin
import bisect

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))


nums = nums[::-1]
dp = [nums[0]]
nums = nums[1:]
for num in nums:
    if dp[-1]<num:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp,num)
        dp[idx] = num

print(N-len(dp))
