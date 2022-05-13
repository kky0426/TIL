from sys import stdin
import sys
sys.setrecursionlimit(10**5)
N,K = map(int,stdin.readline().split())

dp = [-1]*N

nums = list(map(int,stdin.readline().split()))

def solve(idx):
    if idx == N-1:return 1

    if dp[idx]!=-1:return dp[idx]

    res = 0
    for i in range(idx+1,N):
        if (i-idx)*(1+abs(nums[i]-nums[idx])) <= K:
            res+=solve(i)
    dp[idx] = res
    return dp[idx]

solve(0)

print("YES") if dp[0]>0 else print("NO")