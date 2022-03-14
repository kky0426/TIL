from sys import stdin

N = int(stdin.readline())
block = list(stdin.readline().rstrip())

dp = [float("inf")]*(N+1)
dp[1] = 0

for i in range(1,N):
    if block[i-1] == 'B':
        for j in range(i+1,N+1):
            if block[j-1] == 'O':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
    elif block[i-1] == 'O':
        for j in range(i+1,N+1):
            if block[j-1] == 'J':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
    else:
        for j in range(i+1,N+1):
            if block[j-1] == 'B':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)

print(dp[N] if dp[N]!=float("inf") else -1)

