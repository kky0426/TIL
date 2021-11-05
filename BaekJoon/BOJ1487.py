from sys import stdin

N = int(stdin.readline())

arr = list(tuple(map(int,stdin.readline().split())) for _ in range(N))
ans = 0
max_benefit = 0
arr.sort()
for i in range(N):
    price = arr[i][0]
    benefit = 0
    for j in range(N):
        if arr[j][0]>=price:
            if price-arr[j][1]<0:
                continue
            benefit+=price-arr[j][1]
    if max_benefit<benefit:
        ans = price
        max_benefit = benefit

print(ans)
