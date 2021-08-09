from sys import stdin
import bisect

N = int(stdin.readline())

lines = list(map(int,stdin.readline().split()))

dp = [-float('inf')]

for line in lines:
    if line>dp[-1]:
        dp.append(line)
    else:
        idx = bisect.bisect_left(dp,line)
        dp[idx] = line

print(len(lines)-(len(dp)-1))
