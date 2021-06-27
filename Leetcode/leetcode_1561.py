class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans=0
        piles.sort()
        start = 0
        end = len(piles)-2
        while start<end:
            ans+=piles[end]
            start+=1
            end-=2
        return ans
