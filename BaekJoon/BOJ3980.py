from sys import stdin

T = int(stdin.readline())

ans = 0
def solve(idx,count):
    if idx == 11:
        global ans
        ans = max(ans,count)
        return

    for i in range(11):
        if players[idx][i]!= 0 and not visit[i]:
            visit[i]=True
            solve(idx+1,count+players[idx][i])
            visit[i]=False


for _ in range(T):
    ans = 0
    players = [list(map(int,stdin.readline().split())) for _ in range(11)]
    visit = [False]*11
    solve(0,0)
    print(ans)
