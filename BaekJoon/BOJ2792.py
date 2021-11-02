from sys import stdin
import math

N,M = map(int,stdin.readline().split())

jewelry = [int(stdin.readline()) for _ in range(M)]

left = 1
right = max(jewelry)

while left<=right:
    mid = left+(right-left)//2

    count = 0
    for j in jewelry:
        count+= math.ceil(j/mid)

    if count<=N:
        right = mid-1
        ans = mid
    else:
        left = mid+1

print(ans)
