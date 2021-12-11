from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))

ans = 0
while len(nums)>1:
    idx = nums.index(max(nums))
    if idx == 0:
        ans+=abs(nums[idx]-nums[idx+1])
    elif idx == len(nums)-1:
        ans+=abs(nums[idx]-nums[idx-1])
    else:
        ans+=min(abs(nums[idx]-nums[idx+1]),abs(nums[idx]-nums[idx-1]))
    nums.pop(idx)

print(ans)
