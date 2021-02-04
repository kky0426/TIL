def solution(n):
    answer = 0
    dp=[0]*(n+1)
    for i in range(1,n+1):
        if i==0:
            dp[i]=0
        elif i==1:
            dp[i]=1
        else:
            dp[i]=dp[i-1]+dp[i-2]
    answer=dp[n]
    return answer%1234567
