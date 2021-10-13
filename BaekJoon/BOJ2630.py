from sys import stdin

N = int(stdin.readline())
paper = [list(map(int,stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

def solve(x1,y1,x2,y2):
    N = x2-x1
    count = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            count+=paper[i][j]
    if count == 0:
        global white
        white+=1
        return
    if count == N*N:
        global blue
        blue+=1
        return

    solve(x1,y1,x1+N//2,y1+N//2)
    solve(x1,y1+N//2,x1+N//2,y2)
    solve(x1+N//2,y1,x2,y1+N//2)
    solve(x1+N//2,y1+N//2,x2,y2)

solve(0,0,N,N)
print(white)
print(blue)
