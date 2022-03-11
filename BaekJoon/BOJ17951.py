from sys import stdin

N,K = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

left = 0
right = 20*(10**5)

ans = 0
while left<=right:
    mid = (left+right)//2
    s = 0
    count = 0
    for num in nums:
        s+=num
        if s>=mid:
            s=0
            count+=1

    if count>=K:
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)
