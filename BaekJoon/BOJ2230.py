from sys import stdin

N,M = map(int,stdin.readline().split())

nums = [int(stdin.readline()) for _ in range(N)]

nums.sort()
ans = float("inf")
left = 0
right = 1


while left<N and right<N:
    diff = nums[right]-nums[left]

    if diff == M:
        ans = diff
        break

    if diff<M:
        right+=1
        continue
    left+=1
    ans = min(ans,diff)


print(ans)
