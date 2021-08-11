from sys import stdin

R,C,N = map(int,stdin.readline().split())
board=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(R):
    line = stdin.readline().rstrip()
    line=line.replace(".","0")
    line=line.replace("O","3")
    board.append(list(map(int,list(line))))

def count():
    for i in range(R):
        for j in range(C):
            if board[i][j]>0:
                board[i][j]-=1
                if board[i][j] == 0:
                    board[i][j] = -1

def setUp():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                board[i][j] = 3

def explosion():
    queue = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                board[i][j]=0
                queue.append((i,j))

    while queue:
        x,y = queue.pop()
        board[x][y] = 0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                board[nx][ny] = 0

def solve(N):
    if N==0:
        return
    count()
    N-=1

    if N==0:
        return

    flag = True

    for i in range(N):
        if flag:
            count()
            setUp()
            explosion()
        else:
            count()
            explosion()
        flag=not flag

solve(N)
for row in board:
    ans = list(map(str,row))
    for i in range(len(ans)):
        if ans[i] == '0':
            ans[i] ='.'
        else:
            ans[i] = 'O'
    print("".join(ans))

