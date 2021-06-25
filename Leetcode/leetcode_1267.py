class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0]*m
        col = [0]*n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i]+=1
                    col[j]+=1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                # row>2 or col>2 다른 행 또는 열에 컴퓨터가 존재 
                if grid[i][j] == 1 and (row[i]>1 or col[j]>1):
                    ans+=1
        return ans
