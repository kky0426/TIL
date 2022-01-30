from sys import stdin

D = int(stdin.readline())

graph = {0:[1,3],1:[0,2,3],2:[1,3,4,5],3:[0,1,2,5],4:[2,5,6],5:[3,2,4,7],6:[4,7],7:[5,6]}

dp = [[0 for _ in range(8)] for _ in range(D+1)]

dp[0][0] = 1

for i in range(1,D+1):
    for j in range(8):
        for adj in graph[j]:
            dp[i][j] += dp[i-1][adj]
            dp[i][j]%=1000000007

print(dp[D][0])
