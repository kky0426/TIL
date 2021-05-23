class Solution:
    flag=False
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        
        
        def dfs(x,y,word,visit):
            if len(word)==0:
                self.flag=True
                return
            
            if not(0<=x<row and 0<=y<col and word[0]==board[x][y] and visit[x][y]==0):
                return
            
            visit[x][y]=1
            dfs(x+1,y,word[1:],visit)
            dfs(x-1,y,word[1:],visit)
            dfs(x,y+1,word[1:],visit)
            dfs(x,y-1,word[1:],visit)
            visit[x][y]=0
        
        for i in range(row):
            for j in range(col):
                visit=[[0 for _ in range(col)] for _ in range(row)]
                dfs(i,j,word,visit)
                if self.flag==True:
                    return self.flag
            
        
        return self.flag
