from sys import stdin

N = int(stdin.readline())

ans = 0
broken = [False]*1000001
for _ in range(N):
    a,b,c = map(int,stdin.readline().split())
    if (not broken[a]) and (not broken[b]) and (not broken[c]):
        ans+=1
    broken[a] = True
    broken[b] = True
    broken[c] = True

print(ans)