from sys import stdin

T=int(stdin.readline().rstrip())

for _ in range(T):
    K = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().rstrip().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    sum = [0]*(K+1)

    for i in range(1,K+1):
        sum[i]=sum[i-1]+nums[i-1]

    for offset in range(1,K):
        for l in range(K-offset):
            r = l+offset
            dp[l][r]=float("inf")
            for i in range(l,r):
                dp[l][r] = min(dp[l][r],dp[l][i]+dp[i+1][r]+sum[r+1]-sum[l])

    print(dp[0][K-1])
