class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        i=len(num)-1
        while i>=0:
            if int(num[i])%2!=0:
                ans+=num[:i+1]
                break
            i-=1
        return ans
