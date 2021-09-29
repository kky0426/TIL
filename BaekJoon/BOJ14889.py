from sys import stdin

N = int(stdin.readline())

players = [list(map(int,stdin.readline().split())) for _ in range(N)]

idx = [i for i in range(N)]

def combinations(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],n-1):
                yield [arr[i]]+next

total = set(idx)
visit = set()
ans = float("inf")
for blue in combinations(idx,N//2):
    red = total-set(blue)

    red_count = 0
    blue_count = 0
    for i in red:
        for j in red:
            red_count+=players[i][j]

    for i in blue:
        for j in blue:
            blue_count+=players[i][j]

    ans = min(ans,abs(blue_count-red_count))

print(ans)
