from sys import stdin
from collections import defaultdict
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    N,K = map(int,stdin.readline().split())
    times = list(map(int,stdin.readline().split()))
    degree = [0]*N
    graph = defaultdict(list)

    for _ in range(K):
        x,y = map(int,stdin.readline().split())
        graph[x-1].append(y-1)
        degree[y-1]+=1

    W = int(stdin.readline())

    queue=deque()
    for i in range(N):
        if degree[i] == 0:
            queue.append(i)

    dp = [0]*N

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            dp[next] = max(dp[next],dp[node]+times[node])
            degree[next]-=1
            if degree[next] == 0:
                queue.append(next)

    print(dp[W-1]+times[W-1])
