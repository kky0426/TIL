from sys import stdin
import bisect

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
nums.sort()
ans = 0
for i in range(N-2):
    left = i+1
    right = N-1
    while left<right:
        res = nums[left]+nums[right]+nums[i]
        if res<0:
            left+=1
        elif res == 0:
            if nums[left] == nums[right]:
                ans+=right-left
            else:
                idx = bisect.bisect_left(nums,nums[right])
                ans+=right-idx+1
            left+=1
        else:
            right-=1

print(ans)