from sys import stdin

N = 19
grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

def check_row(x,y):
    count = 0
    target = grid[x][y]
    if (x-3>=0 and grid[x-3][y] == target) or (x+3<N and grid[x+3][y] == target):
        return False

    for i in range(x-2,x+3):
        if 0<=i<N and grid[i][y]==target:
            count+=1

    if count == 5:
        return True
    return False


def check_col(x, y):
    count = 0
    target = grid[x][y]
    if (y - 3 >= 0 and grid[x][y-3] == target) or (y + 3 < N and grid[x][y+3] == target):
        return False

    for i in range(y - 2, y + 3):
        if 0 <= i < N and grid[x][i] == target:
            count += 1

    if count == 5:
        return True
    return False

def check_digo_l(x,y):
    count = 0
    target = grid[x][y]
    if (0<=x-3<N and 0<=y-3<N and grid[x-3][y-3] == target) or (0<=x+3<N and 0<=y+3<N and grid[x+3][y+3] == target):
        return False

    for i in range(1,3):
        if 0<=x-i<N and 0<=y-i<N and grid[x-i][y-i] == target:
            count+=1
        if 0<=x+i<N and 0<=y+i<N and grid[x+i][y+i] == target:
            count+=1

    if count == 4:
        return True
    return False


def check_digo_r(x, y):
    count = 0
    target = grid[x][y]
    if (0 <= x + 3 < N and 0 <= y - 3 < N and grid[x + 3][y - 3] == target) or (
            0 <= x - 3 < N and 0 <= y + 3 < N and grid[x - 3][y + 3] == target):
        return False

    for i in range(1, 3):
        if 0 <= x + i < N and 0 <= y - i < N and grid[x + i][y - i] == target:
            count += 1
        if 0 <= x - i < N and 0 <= y + i < N and grid[x - i][y + i] == target:
            count += 1

    if count == 4:
        return True
    return False

row = 0
col = 0
win = 0
flag = False
for i in range(N):
    for j in range(N):
        if grid[i][j]>0:
            if check_row(i,j):
                win = grid[i][j]
                row = i-2
                col = j
                flag = True
                break
            if check_col(i,j):
                win = grid[i][j]
                row = i
                col = j-2
                flag = True
                break

            if check_digo_l(i,j):
                win = grid[i][j]
                row = i-2
                col = j-2
                flag = True
                break

            if check_digo_r(i,j):
                win = grid[i][j]
                row = i+2
                col = j-2
                flag = True
                break
if flag:
    print(win)
    print(row+1,col+1)
else:
    print(win)
