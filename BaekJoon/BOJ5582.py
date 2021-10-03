from sys import stdin

A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

N = len(A)
M = len(B)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

ans = 0

for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+1
            ans = max(ans,dp[i][j])
        else:
            dp[i][j] = 0

print(ans)
