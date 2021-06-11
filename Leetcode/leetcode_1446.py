class Solution:
    def maxPower(self, s: str) -> int:
        dp = [1]*(len(s))
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                dp[i] = dp[i-1]+1
                
        return max(dp)
            
