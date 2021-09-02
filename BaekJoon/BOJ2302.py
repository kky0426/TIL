from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

vips = []
for _ in range(M):
    vips.append(int(stdin.readline()))

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,N):
    dp[i] = dp[i-1]+dp[i-2]

ans = 1
pre = 0
for vip in vips:
    ans*=dp[vip-pre-1]
    pre = vip
ans*=dp[N-pre]
print(ans)
