from sys import stdin

N,K = map(int,stdin.readline().split())

cPoint=[]
for _ in range(N):
    x,y = map(int,stdin.readline().split())
    cPoint.append((x,y))

distance = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        distance[i][j] = abs(cPoint[i][0]-cPoint[j][0])+abs(cPoint[i][1]-cPoint[j][1])

dp = [[float("inf") for _ in range(N)] for _ in range(K+1)]

dp[0][0] = 0
for i in range(1,N):
    dp[0][i] = dp[0][i-1] + distance[i-1][i]

for k in range(1,K+1):
    dp[k][0] = 0
    dp[k][1] = dp[k-1][1]
    dp[k][k] = distance[0][k]
    for i in range(1,N):
        for j in range(1,k):
            if i-j-1 <0 : continue
            dp[k][i] = min(dp[k][i],dp[k-j][i-j-1]+distance[i-j-1][i],dp[k][i-1]+distance[i-1][i])
print(dp)
