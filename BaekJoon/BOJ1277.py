from sys import stdin
from collections import defaultdict,deque
import math
def get_distance(x1,y1,x2,y2):

    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

N,W = map(int,stdin.readline().split())
M = float(stdin.readline())
place = [list(map(int,stdin.readline().split())) for _ in range(N)]
connected = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

for i in range(N-1):
    for j in range(i+1,N):
        dis = get_distance(place[i][0],place[i][1],place[j][0],place[j][1])
        if dis<=M:
            connected[i+1][j+1] = dis
            connected[j+1][i+1] = dis

graph = defaultdict(list)

for _ in range(W):
    u,v = map(int,stdin.readline().split())
    connected[u][v] = 0
    connected[v][u] = 0

distance = [float("inf")]*(N+1)
distance[1] = 0
queue = deque()
queue.append(1)
while queue:
    cur = queue.popleft()
    for n in range(1,N+1):
        dis = connected[cur][n]
        if distance[n]<dis:
            continue
        if distance[cur]+dis< distance[n]:
            distance[n] = distance[cur]+dis
            queue.append(n)
print(math.floor(distance[N]*1000))
