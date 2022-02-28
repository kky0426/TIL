from sys import stdin

N,M = map(int,stdin.readline().split())


ans = []
visit = [False]*(N+1)

def solve():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1,N+1):
        ans.append(i)
        solve()
        ans.pop()

solve()
