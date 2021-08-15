from sys import stdin

N = int(stdin.readline())

hp = list(map(int,stdin.readline().split()))
happiness = list(map(int,stdin.readline().split()))

dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1,N+1):
    current_hp = hp[i-1]
    current_happy = happiness[i-1]
    for j in range(101):
        if j<current_hp:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-current_hp] + current_happy)

print(dp[N][99])
