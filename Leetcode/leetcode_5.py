class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        dp=[[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i]=1
            
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=2
        
        for idx in range(2,len(s)):
            for start in range(len(s)-idx):
                end=start+idx
                if s[start]==s[end] and dp[start+1][end-1]!=0:
                    dp[start][end] = dp[start+1][end-1]+2
                    
        maxNum=max(map(max,dp))
        for i in range(len(dp)):
            if maxNum in dp[i]:
                sIdx,eIdx = i,dp[i].index(maxNum)
        
        
        for i in range(sIdx,eIdx+1):
            ans+=s[i]
        
        return ans
                    
