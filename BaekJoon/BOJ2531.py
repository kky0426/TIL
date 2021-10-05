from sys import stdin

N,D,K,C = map(int,stdin.readline().split())

sushi = [int(stdin.readline()) for _ in range(N)]
sushi.extend(sushi)

ans = 0
for i in range(N+K):
    temp = set(sushi[i:i+K])
    temp.add(C)
    ans = max(ans,len(temp))

print(ans)
