from sys import stdin
from collections import defaultdict

N,K = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))

for i in range(1,N):
    nums[i]+=nums[i-1]

dic = defaultdict(int)

ans = 0
for i in range(N):
    if nums[i] == K:
        ans+=1
    ans+=dic[nums[i]-K]
    dic[nums[i]]+=1

print(ans)