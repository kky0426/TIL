from sys import stdin

N = int(stdin.readline())

nums = list(int(stdin.readline()) for _ in range(N))

dp_lis = [1]*N
dp_lds = [1]*N

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if nums[i]>nums[j]:
            dp_lis[i] = max(dp_lis[i],dp_lis[j]+1)
        if nums[i]<nums[j]:
            dp_lds[i] = max(dp_lds[i],dp_lds[j]+1)

ans = 0
for i in range(N):
    ans = max(ans,dp_lds[i]+dp_lis[i]-1)

print(ans)