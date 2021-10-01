import sys
sys.setrecursionlimit(10**6)
def solution(grid):
    answer = []
    head = [(-1,0),(0,1),(1,0),(0,-1)]
    R = len(grid)
    C = len(grid[0])
    
    def go(x,y,d):
        nx = x+head[d][0]
        ny = y+head[d][1]
        if nx<0:
            nx = R-1
        elif nx>=R:
            nx = 0
        if ny<0:
            ny = C-1
        elif ny>=C:
            ny = 0
        
        return nx,ny
    
    
    def dfs(x,y,d,start_x,start_y,start_d,count):
        visit[x][y][d] = True
        
        nx,ny = go(x,y,d)
        if grid[nx][ny]=='R':
            d=(d+1)%4
        elif grid[nx][ny] == 'L':
            d =(d-1)%4
        
        if nx==start_x and ny == start_y and d==start_d:
            answer.append(count)
            return
        
        if not visit[nx][ny][d]:
            dfs(nx,ny,d,start_x,start_y,start_d,count+1)
            
    visit = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                dfs(i,j,k,i,j,k,1)
    
    answer.sort()
    return answer
