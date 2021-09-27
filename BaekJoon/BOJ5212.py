from sys import stdin

R,C = map(int,stdin.readline().split())

island = [list(stdin.readline().rstrip()) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def check(x,y):
    count=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if island[nx][ny]=='.':
                count+=1
        else:
            count+=1

    if count>=3:
        return True
    return False
queue = []
for i in range(R):
    for j in range(C):
        if island[i][j]=='X' and check(i,j):
            queue.append((i,j))

while queue:
    x,y = queue.pop()
    island[x][y] = '.'

col = ['.']*C
while True:
    if island[0] == col:
        island.pop(0)
    else:
        break
while True:
    if island[-1] == col:
        island.pop()
    else:
        break

while True:
    flag = True
    for i in range(len(island)):
        if island[i][0]=='X':
            flag=False
            break
    if flag:
        for i in range(len(island)):
            island[i].pop(0)
    else:
        break

while True:
    flag = True
    for i in range(len(island)):
        if island[i][-1] == 'X':
            flag=False
            break

    if flag:
        for i in range(len(island)):
            island[i].pop()
    else:
        break

for ans in island:
    print("".join(ans))
