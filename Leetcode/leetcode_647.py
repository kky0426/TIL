class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        ans=0
        dp = [[0 for _ in range(N)] for _ in range(N)]
        # 길이가 2이하
        for i in range(N):
            for j in range(N):
                if i==j:
                    dp[i][j]=1
                elif i+1==j:
                    if s[i]==s[j]:
                        dp[i][j]=1
        #나머지
        for offset in range(2,N):
            for start in range(N-offset):
                end=start+offset
                if s[start]==s[end] and dp[start+1][end-1]==1:
                    dp[start][end]=1
        for i in range(N):
            for j in range(N):
                if dp[i][j]==1:
                    ans+=1
                    
