from sys import stdin

N,S,M = map(int,stdin.readline().split())

song = list(map(int,stdin.readline().split()))

dp = [[False for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = True

for i in range(N):
    for j in range(M+1):
        if dp[i][j]:
            if j+song[i]<=M:
                dp[i+1][j+song[i]] = True
            if j-song[i]>=0:
                dp[i+1][j-song[i]] = True

ans = -1

for i in range(M,-1,-1):
    if dp[N][i]:
        ans = i
        break
print(ans)
