from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
nums.sort()
ans =0

left = 0
right  = N-1

while left<right:
    if nums[left]+nums[right]>M:
        right-=1
    elif nums[left]+nums[right]<M:
        left+=1
    else:
        ans+=1
        left+=1

print(ans)
