from sys import stdin

N,M = map(int,stdin.readline().split())
height = list(map(int,stdin.readline().split()))

left = 0
right = max(height)

while left<=right:
    mid = left+(right-left)//2
    count = 0
    for i in range(N):
        if mid<height[i]:
            count+=height[i]-mid

    if count>=M:
        left = mid+1
        ans = mid
    else:
        right = mid-1

print(ans)
