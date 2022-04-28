from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
K = max(nums)

parent = [-1]*(K+1)
visit = [False]*(K+1)

visit[nums[0]] = True

for i in range(1,N):
    if not visit[nums[i]]:
        visit[nums[i]] = True
        parent[nums[i]] = nums[i-1]

print(K+1)
print(*parent)

