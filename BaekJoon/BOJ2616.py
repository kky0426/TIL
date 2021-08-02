from sys import stdin

N= int(stdin.readline())

trains=list(map(int,stdin.readline().split()))
M = int(stdin.readline())

for i in range(1,len(trains)):
    trains[i]+=trains[i-1]
trains.insert(0,0)
dp=[[0 for _ in range(N+1)] for _ in range(4)]

for i in range(1,4):
    for j in range(M,N+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-M]+trains[j]-trains[j-M])

print(dp[-1][-1])
