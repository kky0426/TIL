from sys import stdin

N,M,L = map(int,stdin.readline().split())

place = list(map(int,stdin.readline().split()))
place.append(0)
place.append(L-1)
place.sort()

left=0
right=L
ans = 0
while left<=right:
    mid = left+(right-left)//2
    count = 0
    for i in range(1,N+2):
        if place[i]-place[i-1]>mid:
            count+=(place[i]-place[i-1]-1)//mid

    if count<=M:
        ans=mid
        right=mid-1
    else:
        left=mid+1

print(ans)
