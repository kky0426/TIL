from sys import stdin

N = int(stdin.readline())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0

def check(r1,c1,r2,c2):
    flag = True
    prev = grid[r1][c1]
    for i in range(r1,r2):
        if not flag:
            break
        for j in range(c1,c2):
            if grid[i][j] != prev:
                flag = False
                break

    return flag

def solve(r1,c1,r2,c2):
    if check(r1,c1,r2,c2):
        global minus,zero,plus
        if grid[r1][c1] == -1:
            minus+=1
        elif grid[r1][c1] == 0:
            zero+=1
        else:
            plus+=1
        return
    else:
        offset = (r2-r1)//3
        solve(r1,c1,r1+offset,c1+offset)
        solve(r1+offset,c1,r1+offset*2,c1+offset)
        solve(r1+offset*2,c1,r1+offset*3,c1+offset)
        solve(r1,c1+offset,r1+offset,c1+offset*2)
        solve(r1+offset,c1+offset,r1+offset*2,c1+offset*2)
        solve(r1+offset*2,c1+offset,r1+offset*3,c1+offset*2)
        solve(r1,c1+offset*2,r1+offset,c1+offset*3)
        solve(r1+offset,c1+offset*2,r1+offset*2,c1+offset*3)
        solve(r1+offset*2,c1+offset*2,r1+offset*3,c1+offset*3)

solve(0,0,N,N)
print(minus)
print(zero)
print(plus)

