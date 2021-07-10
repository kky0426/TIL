class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = list(s.split())
        mLength=0
        for word in words:
            mLength = max(mLength,len(word))
        ans = ["" for _ in range(mLength)]
        
        for word in words:
            for i in range(mLength):
                if i<len(word):
                    ans[i]+=word[i]
                else:
                    ans[i]+=' '
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()
            
        return ans
