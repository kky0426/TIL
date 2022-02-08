from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

nums = [i for i in range(1,N+1)]
nums = deque(nums)

ans = [0]*N

for i in range(1,N+1):
    if N-i <= K:
        ans[i-1] = nums.pop()
        K -= N-i
    else:
        ans[i-1] = nums.popleft()

for n in ans:
    print(n,end=" ")
