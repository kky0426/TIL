from sys import stdin

num = list(map(int,stdin.readline().rstrip()))

N = len(num)
dp = [0]*(N+1)
dp[0],dp[1] = 1,1

if num[0] == 0:
    print(0)
else:
    for i in range(2,N+1):
        if num[i-1]>0:
            dp[i] += dp[i-1]

        if 10<=num[i-2]*10+num[i-1]<=26:
            dp[i] += dp[i-2]
        dp[i]%=1000000
    print(dp[N])
