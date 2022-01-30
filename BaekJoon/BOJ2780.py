from sys import stdin

T = int(stdin.readline())

graph = {0:[7],1:[2,4],2:[1,3,5],3:[2,6],4:[1,5,7],5:[2,4,6,8],6:[3,5,9],7:[4,8,0],8:[5,7,9],9:[6,8]}

dp = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2,1001):
    for j in range(10):
        for adj in graph[j]:
            dp[i][j]+=dp[i-1][adj]
            dp[i][j]%=1234567

for _ in range(T):
    N = int(stdin.readline())
    print(sum(dp[N])%1234567)
