class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans = ""
        if int(n)>=0:
            i=0
            while i<len(n):
                if int(n[i]) < x:
                    ans = n[:i] + str(x) + n[i:]
                    break
                i+=1
            if i == len(n):
                ans = n+str(x)
        else:
            i = 1
            while i<len(n):
                if int(n[i]) > x:
                    ans = n[:i] + str(x) + n[i:]
                    break
                i+=1
            if i==len(n):
                ans = n+str(x)
            
        
        return ans
