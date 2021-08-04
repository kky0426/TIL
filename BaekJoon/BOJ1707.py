from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict


def dfs(node, g):
    visit[node] = g
    for i in graph[node]:
        if visit[i] == 0:
            if not dfs(i, -g):
                return False
        elif visit[node] == visit[i]:
            return False
    return True

K = int(stdin.readline())
for _ in range(K):
    V,E = map(int,stdin.readline().split())
    visit = [0]*(V+1)
    graph = defaultdict(list)

    for _ in range(E):
        s,e = map(int,stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    flag = True

    for node in graph:
        if visit[node] == 0:
            flag = dfs(node,1)
            if not flag:
                break
    print('YES' if flag else 'NO')
