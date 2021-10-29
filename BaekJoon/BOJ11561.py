from sys import stdin

T = int(stdin.readline());

for _ in range(T):
    N = int(stdin.readline())

    left = 0
    right = N
    ans = 0
    while left<=right:
        mid = left+(right-left)//2

        if mid*(mid+1)/2 <= N:
            left = mid+1
            ans = mid
        else:
            right = mid-1
    print(ans)
