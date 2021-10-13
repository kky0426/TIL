from sys import stdin

N,M = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]

window = min(N,M)
flag = False
while window>0 and not flag:
    for i in range(N-window+1):
        for j in range(M-window+1):
            if grid[i][j] == grid[i][j+window-1] == grid[i+window-1][j] == grid[i+window-1][j+window-1]:
                print(window**2)
                flag = True
                break
        if flag:
            break
    window-=1
