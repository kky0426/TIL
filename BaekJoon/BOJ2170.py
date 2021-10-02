from sys import stdin

N = int(stdin.readline())

line = [tuple(map(int,stdin.readline().split())) for _ in range(N)]

left = -float("inf")
right = -float("inf")
line.sort()
ans = []
for l,r in line:
    if right<l:
        ans.append(right-left)
        left = l
        right = r
    else:
        right = max(right,r)
ans.append(right-left)
print(sum(ans[1:]))
