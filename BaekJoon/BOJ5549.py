from sys import stdin

N,M = map(int,stdin.readline().split())
K = int(stdin.readline())

ice = [[0 for _ in range(M+1)] for _ in range(N+1)]
jungle = [[0 for _ in range(M+1)] for _ in range(N+1)]
sea = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    line = stdin.readline().rstrip()
    for j in range(1,M+1):
        if line[j-1] == 'J':
            jungle[i][j]+=1
        elif line[j-1] == 'O':
            sea[i][j]+=1
        else:
            ice[i][j]+=1

for i in range(1,N+1):
    for j in range(1,M+1):
        ice[i][j]+=ice[i][j-1]
        jungle[i][j]+=jungle[i][j-1]
        sea[i][j]+=sea[i][j-1]

for i in range(1,N+1):
    for j in range(1,M+1):
        ice[i][j]+=ice[i-1][j]
        jungle[i][j]+=jungle[i-1][j]
        sea[i][j]+=sea[i-1][j]

for _ in range(K):
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    j = jungle[x2][y2]-jungle[x1-1][y2]-jungle[x2][y1-1]+jungle[x1-1][y1-1]
    s = sea[x2][y2]-sea[x1-1][y2]-sea[x2][y1-1]+sea[x1-1][y1-1]
    i = ice[x2][y2]-ice[x1-1][y2]-ice[x2][y1-1]+ice[x1-1][y1-1]
    print(j,s,i)