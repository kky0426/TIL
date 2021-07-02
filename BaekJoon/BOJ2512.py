from sys import stdin

N = int(stdin.readline().rstrip())
ans = 0
req = list(map(int,stdin.readline().rstrip().split()))
M = int(stdin.readline().rstrip())

left = 1
right = max(req)

while left<=right:
    mid = left+(right-left)//2
    count = 0
    for money in req:
        if money>mid:
            count+=mid
        else:
            count+=money
    if count<=M:
        left = mid+1
        ans = mid
    else:
        right = mid-1

print(ans)
