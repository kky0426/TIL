from sys import stdin
from itertools import permutations
from collections import deque

N,K = map(int,stdin.readline().split())
nums = [n for n in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int,stdin.readline().split())))



for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


path_list = list(permutations(nums[:K]+nums[K+1:],N-1))

ans = float("inf")

while path_list:
    path = deque(path_list.pop())
    path.appendleft(K)
    wegiht = 0
    for i in range(1,len(path)):
        wegiht+=graph[path[i-1]][path[i]]
    ans = min(ans,wegiht)

print(ans)
