from sys import stdin

N = int(stdin.readline())

bus = [list(map(int,stdin.readline().split())) for _ in range(N)]

bus.sort(key=lambda x:x[0])


ans = []
left,right,cost = bus[0]

for s,e,c in bus[1:]:
    if right<s:
        ans.append((left,right,cost))
        left=s
        right=e
        cost = c
    else:
        right = max(right,e)
        cost = min(cost,c)

ans.append((left,right,cost))

print(len(ans))
for arr in ans:
    print(*arr)
