from sys import stdin

N,D = map(int,stdin.readline().split())

road = [list(map(int,stdin.readline().split())) for _ in range(N)]

road.sort()

dp=[i for i in range(D+1)]

for s,e,d in road:
    if e<=D:
        dp[e] = min(dp[s]+d,dp[e])

    for j in range(s,D+1):
        dp[j] = min(dp[j-1]+1,dp[j])

print(dp[-1])
