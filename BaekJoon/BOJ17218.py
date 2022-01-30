from sys import stdin

A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

N = len(A)
M = len(B)

dp = [[0 for _ in range(M+1)]for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

count = dp[N][M]

i = N
j = M
ans = ""
while count>0:
    if A[i-1] == B[j-1]:
        ans+=A[i-1]
        i-=1
        j-=1
        count-=1
    else:
        if dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1

ans = ans[::-1]
print(ans)
