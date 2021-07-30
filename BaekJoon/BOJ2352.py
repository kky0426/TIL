from sys import stdin
import bisect

N = int(stdin.readline())

nums=list(map(int,stdin.readline().split()))

dp=[-float('inf')]

for num in nums:
    if dp[-1]<num:
        dp.append(num)
    else:
        idx=bisect.bisect_left(dp,num)
        dp[idx]=num

print(len(dp)-1)
