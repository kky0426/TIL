from sys import stdin

N,M = map(int,stdin.readline().split())


ans = []
visit = [False]*(N+1)

def solve(num):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(num,N+1):
        if not visit[i]:
            visit[i]=True
            ans.append(i)
            solve(i)
            ans.pop()
            visit[i]=False

solve(1)
