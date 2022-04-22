from sys import stdin
from collections import defaultdict,deque

N = int(stdin.readline())
graph = defaultdict(list)
for i in range(N):
    line = list(map(int,stdin.readline().split()))
    graph[i+1].extend(line[:len(line)-1])

M = int(stdin.readline())

start = list(map(int,stdin.readline().split()))

time = [-1]*(N+1)
queue = deque()
for p in start:
    queue.append((p,0))

while queue:
    n,t = queue.popleft()
    if time[n] == -1:
        time[n] = t
    else:
        time[n] = min(time[n],t)

    for node in graph[n]:
        if time[node]>=0:
            continue
        count = 0
        for adj in graph[node]:
            if time[adj]>=0:
                count+=1

        if count == 0:
            continue

        if count*2>=len(graph[node]):
            queue.append((node,t+1))

print(*time[1:])
