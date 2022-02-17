from sys import stdin

T = int(stdin.readline())

parent = []
dis = []

def find(x):
    if parent[x] == x:
        return x
    else:
        temp = find(parent[x])
        dis[x] += dis[parent[x]]
        parent[x] = temp
        return parent[x]


def union(x,y):
    dis[x] = abs(x-y)%1000
    parent[x] = y

for _ in range(T):
    N = int(stdin.readline())
    parent = [i for i in range(N+1)]
    dis = [0]*(N+1)

    while True:
        line = list(stdin.readline().split())
        if line[0] == 'E':
            find(int(line[1]))
            print(dis[int(line[1])])
        elif line[0] == 'I':
            union(int(line[1]),int(line[2]))
        else:
            break
