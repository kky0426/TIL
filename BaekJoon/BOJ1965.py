from sys import stdin
import bisect

N = int(stdin.readline())
box = list(map(int,stdin.readline().split()))

dp = [-float("inf")]

for i in box:
    if dp[-1]<i:
        dp.append(i)
    else:
        idx = bisect.bisect_left(dp,i)
        dp[idx] = i

print(len(dp)-1)
