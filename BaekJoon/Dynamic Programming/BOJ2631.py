import sys
N = int(input())

child=[]

for i in range(N):
    child.append(int(sys.stdin.readline()))

dp=[1]*N

for i in range(N):
    for j in range(i):
        if child[i] > child[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(N-max(dp))
