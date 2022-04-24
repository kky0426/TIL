from sys import stdin
from collections import deque,defaultdict

times = {}
ans = [0]*26
graph = defaultdict(list)
indegree = {}
while True:
    try:
        line = list(stdin.readline().split())
        if len(line) < 3:
            task,time = line[0],int(line[1])
            times[task] = time
            indegree[task] = 0
        else:
            task,time,adj = line[0],int(line[1]),line[2]
            times[task] = time
            for ch in adj:
                graph[ch].append(task)
            indegree[task] = len(adj)
    except:
        break

queue = deque()
for k,v in indegree.items():
    if v == 0:
        queue.append(k)
        ans[ord(k)-ord('A')] = times[k]
while queue:
    cur = queue.popleft()
    for ch in graph[cur]:
        ans[ord(ch)-ord('A')] = max(ans[ord(cur)-ord('A')]+times[ch],ans[ord(ch)-ord('A')])
        indegree[ch] -= 1
        if indegree[ch] == 0:
            queue.append(ch)

print(max(ans))




