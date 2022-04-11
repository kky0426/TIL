from sys import stdin

N = int(stdin.readline())

arr = [list(map(int,stdin.readline().split())) for _ in range(N)]


def solve(x,y,N):
    if N == 2:
        temp = [arr[x][y],arr[x+1][y],arr[x][y+1],arr[x+1][y+1]]
        temp.sort()
        return temp[2]
    else:
        lt = solve(x,y,N//2)
        lb = solve(x+N//2,y,N//2)
        rt = solve(x,y+N//2,N//2)
        rb = solve(x+N//2,y+N//2,N//2)
        temp = [lt,lb,rt,rb]
        temp.sort()
        return temp[2]

print(solve(0,0,N))

