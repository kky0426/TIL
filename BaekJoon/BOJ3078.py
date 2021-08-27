from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

dp = [deque() for _ in range(21)]

ans = 0

for i in range(N):
    length = len(stdin.readline().rstrip())
    while dp[length] and i-dp[length][0]>K:
        dp[length].popleft()

    if dp[length]:
        ans+=len(dp[length])
    dp[length].append(i)

print(ans)
