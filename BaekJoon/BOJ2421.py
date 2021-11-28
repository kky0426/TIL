from sys import stdin

N = int(stdin.readline())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

prime = [1]*(int(str(N)+str(N))+1)
prime[0]=0
prime[1]=0

for i in range(2,len(prime)):
    if prime[i] == 1:
        for j in range(2*i,len(prime),i):
            prime[j] = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+prime[int(str(i)+str(j))]

print(dp[-1][-1]-1)
