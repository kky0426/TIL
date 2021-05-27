class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start,end=0,1
        profit=0
        while end<len(prices):
            if prices[start]>prices[end]:
                start+=1
                end+=1
            else:
                if end==len(prices)-1:
                    profit+=prices[end]-prices[start]
                    break
                if prices[end]<prices[end+1]:
                    end=end+1
                else:
                    profit+=prices[end]-prices[start]
                    start=end+1
                    end=start+1
        
        return profit
