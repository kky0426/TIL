from sys import stdin
from itertools import combinations

N = int(stdin.readline())

empty = []
board = []
for i in range(N):
    line = list(stdin.readline().split())
    board.append(line)
    for j in range(N):
        if line[j] == 'X':
            empty.append((i,j))

def gamsi(x,y):
    count = 0

    for i in range(x+1,N):
        if board[i][y] == 'S':
            count+=1
        elif board[i][y] == 'O':
            break

    for i in reversed(range(0,x)):
        if board[i][y] == 'S':
            count+=1
        elif board[i][y] == 'O':
            break

    for i in range(y+1,N):
        if board[x][i] == 'S':
            count+=1
        elif board[x][i] == 'O':
            break

    for i in reversed(range(0,y)):
        if board[x][i] == 'S':
            count+=1
        elif board[x][i] == 'O':
            break
    return count

cases = list(combinations(empty,3))

flag=False
for case in cases:
    if flag:
        break
    x1,y1 = case[0][0],case[0][1]
    x2, y2 = case[1][0], case[1][1]
    x3, y3 = case[2][0], case[2][1]

    board[x1][y1] = 'O'
    board[x2][y2] = 'O'
    board[x3][y3] = 'O'

    count=0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'T':
                count+=gamsi(i,j)

    board[x1][y1] = 'X'
    board[x2][y2] = 'X'
    board[x3][y3] = 'X'

    if count == 0:
        flag=True

print("YES" if flag else "NO")
