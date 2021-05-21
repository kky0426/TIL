class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            best=2**31-1
            for coin in coins:
                if coin<=i and dp[i-coin]!=-1:
                    best=min(best,dp[i-coin])
            if best==2**31-1:
                dp[i]=-1
            else:
                dp[i]=best+1
        return dp[-1]
