from sys import stdin

N = int(stdin.readline())

nums = [int(stdin.readline()) for _ in range(N)]

ans = 0
nums.sort()
for i in range(1,N+1):
    ans+=abs(i-nums[i-1])

print(ans)
