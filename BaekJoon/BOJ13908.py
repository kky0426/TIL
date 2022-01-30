from sys import stdin
N,M = map(int,stdin.readline().split())

nums = []
if M != 0:
    nums = list(map(int,stdin.readline().split()))

visit = [False]*10

for n in nums:
    visit[n] = True

ans = 0
def solve(idx,count):
    if idx == N:
        if count == M:
            global ans
            ans+=1
            return
        return

    for i in range(10):
        if visit[i]:
            visit[i] = False
            solve(idx+1,count+1)
            visit[i] = True
        else:
            solve(idx+1,count)

solve(0,0)
print(ans)
