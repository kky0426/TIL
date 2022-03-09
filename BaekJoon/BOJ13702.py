from sys import stdin

N,K = map(int,stdin.readline().split())

mak = [int(stdin.readline()) for _ in range(N)]

left = 1
right = max(mak)

ans = 0

while left<=right:
    mid = (left+right)//2
    count = 0
    for l in mak:
        count+=l//mid

    if count>=K:
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)