from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    global ans
    visit[x] = 1
    next = people[x]
    cycle.append(x)

    if visit[next]:
        if next in cycle:
            ans+=cycle[cycle.index(next):]
        return
    else:
        dfs(next)

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())

    people =[0]+list(map(int,stdin.readline().split()))
    visit = [0]*(N+1)


    ans = []
    for i in range(1,N+1):
        if visit[i] == 0:
            cycle=[]
            dfs(i)
    print(N-len(ans))
