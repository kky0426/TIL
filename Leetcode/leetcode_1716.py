class Solution:
    def totalMoney(self, n: int) -> int:
        start=1
        ans = 0
        for i in range(n):
            if i!=0 and i%7==0:
                start+=1
            ans+= start+(i%7)
        return ans
