import sys
import copy
sys.setrecursionlimit(100000)
N = int(input())

mat = []
for i in range(N):
    mat.append(list(sys.stdin.readline().rstrip()))


def dfs(x, y, color, mat):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == color:
            mat[nx][ny] = '0'
            dfs(nx, ny, color, mat)


def print_RGB(matix):
    mat=copy.deepcopy(matix)
    count=0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'R':
                dfs(i, j, 'R', mat)
                count += 1
            elif mat[i][j] == 'G':
                dfs(i, j, 'G', mat)
                count += 1
            elif mat[i][j] == 'B':
                dfs(i, j, 'B', mat)
                count += 1
    return count

def print_RB(matix):
    count=0
    mat=copy.deepcopy(matix)
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'G':
                mat[i][j] = 'R'
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'R':
                dfs(i, j, 'R', mat)
                count += 1
            elif mat[i][j] == 'B':
                dfs(i, j, 'B', mat)
                count += 1

    return count

print(print_RGB(mat),print_RB(mat))
