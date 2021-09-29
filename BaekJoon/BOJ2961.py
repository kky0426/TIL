from sys import stdin

N = int(stdin.readline())

taste = [list(map(int,stdin.readline().split())) for _ in range(N)]

ans = float("inf")
for i in range(1,1<<N):
    sin = 1
    ssen = 0
    for j in range(N):
        if i&(1<<j):
            sin*=taste[j][0]
            ssen+=taste[j][1]
    ans = min(ans,abs(sin-ssen))

print(ans)
