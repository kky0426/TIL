from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()

N = len(s1)
M = len(s2)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][0] = i
for i in range(1,M+1):
    dp[0][i] = i

for i in range(1,N+1):
    for j in range(1,M+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1


print(dp[-1][-1])