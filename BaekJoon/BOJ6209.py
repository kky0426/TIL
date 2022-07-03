from sys import stdin

d,N,M = map(int,stdin.readline().split())

rock = [int(stdin.readline()) for _ in range(N)]
rock.sort()
rock.append(d)


left = 0
right = 1000000001

while left<=right:
    mid = (left+right)//2

    count = 0
    pre = 0
    for r in rock:
        if r-pre>mid:
            pre = r
            count+=1

    if count>N-M:
        left = mid+1
    else:
        ans = mid
        right = mid-1

print(ans)
