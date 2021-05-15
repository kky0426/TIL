from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M=len(grid)
        N=len(grid[0])
    
        
        def bfs(row,col):
            dx=[1,-1,0,0]
            dy=[0,0,1,-1]
            queue=deque()
            queue.append((row,col))
            while queue:
                x,y=queue.popleft()
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<M and 0<=ny<N and grid[nx][ny]=='1':
                        queue.append((nx,ny))
                        grid[nx][ny]='0'
        count=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    bfs(i,j)
                    count+=1
        return count
