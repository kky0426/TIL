class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        
        dp=[[0 for _ in range(col+1)] for _ in range(row+1)]
        
        for i in range(1,row+1):
            dp[i][1]=dp[i-1][1]+grid[i-1][0]
        
        for i in range(1,col+1):
            dp[1][i]=dp[1][i-1]+grid[0][i-1]    
            
        for i in range(2,row+1):
            for j in range(2,col+1):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[-1][-1]
