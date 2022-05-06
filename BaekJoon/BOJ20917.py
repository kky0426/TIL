from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N,S = map(int,stdin.readline().split())
    nums = list(map(int,stdin.readline().split()))
    nums.sort()
    left = 0
    right = 1000000001

    while left<=right:
        mid = (left+right)//2
        count = 1
        pre = nums[0]
        for i in range(1,N):
            if nums[i]-pre>=mid:
                count+=1
                pre = nums[i]
        if count>=S:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    print(ans)