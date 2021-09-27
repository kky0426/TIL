from sys import stdin

C,N = map(int,stdin.readline().split())

INF = float("inf")
dp = [INF]*(C+100)
dp[0] = 0

city = [list(map(int,stdin.readline().split())) for _ in range(N)]

for cost,people in city:
    for i in range(people,len(dp)):
        dp[i] = min(dp[i],dp[i-people]+cost)

print(min(dp[C:]))
