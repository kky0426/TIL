from sys import stdin

K,N,F = map(int,stdin.readline().split())

friend = [[False for _ in range(N+1)] for _ in range(N+1)]
for _ in range(F):
    u,v = map(int,stdin.readline().split())
    friend[u][v] = True
    friend[v][u] = True



flag = False
ans = []
def solve(idx,cnt):
    global flag
    if flag:
        return

    if cnt == K:
        flag=True
        for a in ans:
            print(a)
        return

    for i in range(idx+1,N+1):
        if visit[i]: continue
        is_friend = True

        for a in ans:
            if not friend[a][i]:
                is_friend = False
                break

        if is_friend:
            visit[i] = True
            ans.append(i)
            solve(i,cnt+1)
            ans.pop()
            visit[i] = False


visit = [False]*(N+1)
for i in range(1,N+1):
    if flag:continue
    visit[i] = True
    ans.append(i)
    solve(i,1)
    visit[i] = False
    ans.pop()
if not flag:
    print(-1)