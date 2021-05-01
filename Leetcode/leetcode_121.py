class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num=10001
        profit=0
        for i in range(len(prices)):
            min_num=min(prices[i],min_num)
            profit=max(profit,prices[i]-min_num)
        return profit
