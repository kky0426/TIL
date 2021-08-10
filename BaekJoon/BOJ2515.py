from sys import stdin
import bisect

N,S = map(int,stdin.readline().split())

pictures=[]
hegiht=[]
for _ in range(N):
    h,v = map(int,stdin.readline().split())
    pictures.append((h,v))
    hegiht.append(h)

pictures.sort(key=lambda x:x[0])
hegiht.sort()

dp = [0]*(N+1)

for i in range(1,N+1):
    prev = pictures[i-1][0]-S
    idx = bisect.bisect_right(hegiht,prev)
    dp[i] = max(dp[idx]+pictures[i-1][1],dp[i-1])

print(dp[-1])
