class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans =""
        asc = 96
        while n>0:
            if k-n>=26:
                ans+=chr(asc+26)
                k-=26
            else:
                ans+=chr(asc+k-n+1)
                k=n-1
            n-=1
        return ans[::-1]
