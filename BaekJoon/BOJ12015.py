from sys import stdin
import bisect

N=int(stdin.readline())

nums=list(map(int,stdin.readline().split()))

ans=[-float('inf')]

for i in range(len(nums)):
    if ans[-1]<nums[i]:
        ans.append(nums[i])
    else:
        idx = bisect.bisect_left(ans,nums[i])
        ans[idx]=nums[i]
print(len(ans)-1)
