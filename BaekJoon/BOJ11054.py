from sys import stdin

N=int(stdin.readline())

nums=list(map(int,stdin.readline().split()))

dp1=[0]*N
dp2=[0]*N

for i in range(N):
    for j in range(i):
        if nums[i]>nums[j] and dp1[i]<dp1[j]:
            dp1[i] = dp1[j]
        dp1[i]+=1
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if nums[i]>nums[j] and dp2[i]<dp2[j]:
            dp2[i] = dp2[j]
        dp2[i]+=1
ans=0
for i in range(N):
    ans = max(ans,dp1[i]+dp2[i])
print(ans-1)
