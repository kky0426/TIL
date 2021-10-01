from sys import stdin

N,K = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))
nums.sort()
ans = 0

k = 0
for i in range(N):
    ans+=nums[i]*k
    if k<K:
        k+=1

print(ans)
