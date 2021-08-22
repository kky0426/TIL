from sys import stdin
import bisect

N = int(stdin.readline())

connect = []
for _ in range(N):
    u,v = map(int,stdin.readline().split())
    connect.append((u,v))

connect.sort(key=lambda x:x[0])
dp = [-float("inf")]

for _,num in connect:
    if dp[-1]<num:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp,num)
        dp[idx] = num

print(N-(len(dp)-1))
