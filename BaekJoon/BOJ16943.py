from sys import stdin

A,B = map(int,stdin.readline().split())

num = list(str(A))
N = len(num)
visit = [False]*N
ans = -1
def dfs(string):
    if len(string) == N:
       global ans
       if int(string)<B:
            ans = max(ans,int(string))
       return

    for i in range(N):
        if not visit[i]:
            if string == "" and num[i] == '0':
                continue
            visit[i] = True
            dfs(string+num[i])
            visit[i] = False

dfs("")
print(ans)