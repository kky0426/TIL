from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    coins = list(map(int,stdin.readline().split()))
    M = int(stdin.readline())
    dp=[0]*(M+1)
    dp[0]=1

    for coin in coins:
        for i in range(1,M+1):
            if i>=coin:
                dp[i] += dp[i-coin]

    print(dp[M])
