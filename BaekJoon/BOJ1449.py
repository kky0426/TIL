from sys import stdin

N,M = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))
nums.sort()
left = nums[0]
right = nums[0]+M
ans = 1

for i in range(N):
    if left<=nums[i]<right:
        continue
    else:
        left = nums[i]
        right = nums[i]+M
        ans+=1

print(ans)
