from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
nums.sort()
for i in range(1,N):
    nums[i]+=nums[i-1]
print(sum(nums))
