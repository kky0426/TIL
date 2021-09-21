from sys import stdin

N = int(stdin.readline())

eggs = [list(map(int,stdin.readline().split())) for _ in range(N)]

visit = [False]*N

ans = 0
def dfs(idx,eggs):
    if idx == N:
        count = 0
        for n,_ in eggs:
            if n<=0:
                count+=1
        global ans
        ans = max(ans,count)
        return

    if eggs[idx][0]<=0:
        dfs(idx+1,eggs)
    else:
        for i in range(len(eggs)):
            flag = False
            if i == idx or eggs[i][0]<=0:
                continue

            eggs[idx][0]-=eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            flag = True
            dfs(idx+1,eggs)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

        if not flag:
            dfs(idx+1,eggs)

dfs(0,eggs)
print(ans)
