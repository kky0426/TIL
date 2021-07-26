from sys import stdin
from collections import deque

N=int(stdin.readline())

graph =[[] for _ in range(N+1)]
degree = [0]*(N+1)
time = [0]*(N+1)
dp=[0]*(N+1)

for i in range(1,N+1):
    line = list(map(int,stdin.readline().rstrip().split()))
    time[i] = line[0]
    for j in line[1:-1]:
        graph[j].append(i)
    degree[i]=len(line[1:-1])

queue=deque()
for i in range(1,N+1):
    if degree[i]==0:
        queue.append(i)
        dp[i]=time[i]

while queue:
    node = queue.popleft()
    for d in graph[node]:
        degree[d]-=1
        dp[d]=max(dp[node]+time[d],dp[d])
        if degree[d]==0:
            queue.append(d)

for ans in dp[1:]:
    print(ans)
