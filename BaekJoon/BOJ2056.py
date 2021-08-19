from sys import stdin
from collections import deque
from collections import defaultdict

N = int(stdin.readline())
dp = [0]*(N+1)

degree = [0]*(N+1)

tasks = defaultdict(list)
times = [0]
for i in range(1,N+1):
    line = list(map(int,stdin.readline().split()))
    times.append(line[0])
    degree[i] = line[1]
    for num in line[2:]:
        tasks[num].append(i)

queue = deque()

for i in range(1,N+1):
    if degree[i] == 0:
        queue.append(i)
        dp[i] = times[i]


while queue:
    current = queue.popleft()
    for node in tasks[current]:
        degree[node]-=1
        dp[node] = max(dp[node],dp[current]+times[node])
        if degree[node] == 0:
            queue.append(node)

print(max(dp))
