from sys import stdin

N,S = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))

ans = 0

for i in range(1,1<<N):
    sum_ = 0
    for j in range(N):
        if i&(1<<j):
            sum_+=nums[j]

    if sum_ == S:
        ans+=1

print(ans)
