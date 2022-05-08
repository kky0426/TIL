from sys import stdin

N,Q = map(int,stdin.readline().split())

nums = [0]+list(map(int,stdin.readline().split()))
nums.sort()

for i in range(1,len(nums)):
    nums[i]+=nums[i-1]

for _ in range(Q):
    l,r = map(int,stdin.readline().split())
    print(nums[r]-nums[l-1])
