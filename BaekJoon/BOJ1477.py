from sys import stdin

N,M,L = map(int,stdin.readline().split())

spot = list(map(int,stdin.readline().split()))
spot.append(0)
spot.append(L)
spot.sort()

left = 1
right = L
ans = 0
while left<=right:
    mid = (left+right)//2
    count = 0
    for i in range(1,N+2):
        if spot[i]-spot[i-1]>mid:
            count+=(spot[i]-spot[i-1]-1)//mid
    if count<=M:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(ans)