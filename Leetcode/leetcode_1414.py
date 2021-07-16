class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp=[1,1]
        ans=0
        while True:
            dp.append(dp[-1]+dp[-2])
            if dp[-1] >= k:
                break
        
        for i in reversed(range(len(dp))):
            if dp[i]<=k:
                k-=dp[i]
                ans+=1
            if k==0:
                break
        return ans
