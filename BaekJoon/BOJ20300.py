from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
nums.sort()

ans = 0
if N%2 == 0:
    left = 0
    right = N-1
    while left<right:
        ans = max(ans,nums[left]+nums[right])
        left+=1
        right-=1
else:
    ans = nums[-1]
    left = 0
    right = N-2
    while left<right:
        ans = max(ans,nums[left]+nums[right])
        left+=1
        right-=1

print(ans)