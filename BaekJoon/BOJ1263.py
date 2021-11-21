from sys import stdin

N = int(stdin.readline())
task = [list(map(int,stdin.readline().split())) for _ in range(N)]

task.sort(key=lambda x:x[1],reverse=True)

ans = task[0][1]-task[0][0]

for i in range(1,N):
    if ans<=task[i][1]:
        ans-=task[i][0]
    else:
        ans = task[i][1]-task[i][0]

print(ans if ans>=0 else -1)
