from sys import stdin

N=int(stdin.readline())

nums=list(map(int,stdin.readline().split()))

dp=[1]*N

for i in range(len(nums)):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
