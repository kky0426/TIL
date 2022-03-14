from sys import stdin

N = int(stdin.readline())

arr = [0]+[int(stdin.readline()) for _ in range(N)]

def dfs(n,count):
    visit[n] = True
    if not visit[arr[n]]:
        count = dfs(arr[n],count+1)
    return count

ans = 0
count = 0

for i in range(1,N+1):
    visit = [False]*(N+1)
    c = dfs(i,0)
    if c>count:
        count = c
        ans = i

print(ans)