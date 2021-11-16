from sys import stdin
from collections import deque

N = int(stdin.readline())

people = [0]
for _ in range(N):
    hate = list(map(int,stdin.readline().split()))
    people.append(hate[1:])

team = [[],[]]
visit = [False]*(N+1)
def bfs(node):
    flag = 0
    queue = deque()
    queue.append(node)
    visit[node] = True

    while queue:
        for n in queue:
            team[flag].append(n)

        for _ in range(len(queue)):
            node = queue.popleft()
            for next_node in people[node]:
                if not visit[next_node]:
                    visit[next_node] = True
                    queue.append(next_node)
        flag = flag^1

for i in range(1,N+1):
    if not visit[i]:
        bfs(i)

for i in range(2):
    print(len(team[i]))
    print(*sorted(team[i]))

