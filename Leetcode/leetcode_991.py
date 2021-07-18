class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        ans=0
        while y>x:
            ans+=1
            if y%2==0:
                y=y//2
            else:
                y+=1
            
        return ans+x-y
