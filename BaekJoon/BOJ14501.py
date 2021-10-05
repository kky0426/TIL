from sys import stdin

N = int(stdin.readline())
task = [list(map(int,stdin.readline().split())) for _ in range(N)]

dp = [0]*(N+1)

for i in range(1,N+1):
    t,p = task[i-1]
    if i+t-1<=N:
        dp[i+t-1] = max(dp[i+t-1],max(dp[:i])+p)

print(max(dp))
