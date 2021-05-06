from sys import stdin

N = int(stdin.readline().rstrip())
nums=list(stdin.readline().rstrip().split())
M=int(stdin.readline().rstrip())

dp=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i]=1

for j in range(N-1):
    if nums[j]==nums[j+1]:
        dp[j][j+1]=1

for idx in range(2,len(nums)):
    for start in range(len(nums)):
        end=start+idx
        if end>=N:
            break
        if nums[start]==nums[end] and dp[start+1][end-1]==1:
            dp[start][end]=1

for _ in range(M):
    s,e=map(int,stdin.readline().rstrip().split())
    print(dp[s-1][e-1])
