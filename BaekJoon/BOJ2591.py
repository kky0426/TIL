from sys import stdin

nums = list(stdin.readline().rstrip())

N = len(nums)
dp = [0]*(N+1)
if nums[0] == '0':
    print(0)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if nums[i-1] != '0':
            dp[i]+=dp[i-1]
            if 10<=int(nums[i-2]+nums[i-1])<=34:
                dp[i]+=dp[i-2]
        else:
            if 10<=int(nums[i-2]+nums[i-1])<=34:
                dp[i]+=dp[i-2]

    print(dp[N])


