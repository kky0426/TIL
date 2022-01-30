from sys import stdin

N,P = map(int,stdin.readline().split())


stack = [[] for _ in range(N+1)]
ans = 0
for _ in range(N):
    line,pret = map(int,stdin.readline().split())
    while stack[line] and stack[line][-1]>pret:
        stack[line].pop()
        ans+=1
    if stack[line] and stack[line][-1] == pret:
        continue
    stack[line].append(pret)
    ans+=1

print(ans)
