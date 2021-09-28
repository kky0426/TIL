from sys import stdin

N,M = map(int,stdin.readline().split())

nums = [0]+list(map(int,stdin.readline().split()))
for i in range(N):
    nums[i+1]+=nums[i]

for _ in range(M):
    s,e = map(int,stdin.readline().split())
    print(nums[e]-nums[s-1])

