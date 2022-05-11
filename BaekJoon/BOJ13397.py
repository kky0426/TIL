from sys import stdin

N,M = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

left = 0
right = max(nums) - min(nums)

while left<=right:
    mid = left+(right-left)//2

    count = 1
    min_num = float("inf")
    max_num = 0
    for num in nums:
        min_num = min(min_num,num)
        max_num = max(max_num,num)
        if max_num-min_num > mid:
            min_num = num
            max_num = num
            count+=1
    if count<=M:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(ans)