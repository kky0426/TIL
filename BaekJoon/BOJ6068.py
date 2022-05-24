from sys import stdin

N = int(stdin.readline())
task = [list(map(int,stdin.readline().split())) for _ in range(N)]

task.sort(key = lambda x:x[1],reverse=True)


time = 1000001
for t,s in task:
    if time>=s:
        time = s-t
    else:
        time = time-t

print(time if time>=0 else -1)