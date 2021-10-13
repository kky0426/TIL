from sys import stdin

X,Y = map(int,stdin.readline().split())
Z = Y*100//X
ans = -1
if X==Y:
    print(-1)
else:
    left = 0
    right = X
    while left<=right:
        mid = left+(right-left)//2
        rate = (Y+mid)*100//(X+mid)
        if rate==Z:
            left = mid+1
        else:
            ans = mid
            right = mid-1

    print(ans)
