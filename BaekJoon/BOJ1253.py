from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
nums.sort()

ans = 0
for i in range(N):
    target = nums[i]
    l = 0
    r = N-1
    while l<r:
        if l == i:
            l+=1
            continue

        if r == i:
            r-=1
            continue

        if nums[l]+nums[r] == target:
            ans+=1
            break
        elif nums[l]+nums[r] > target:
            r-=1
        else:
            l+=1

print(ans)