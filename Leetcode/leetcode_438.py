class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        ofs=len(p)
        compare=list(p)
        compare.sort()
        for i in range(len(s)-ofs+1):
            temp=list(s[i:i+ofs])
            temp.sort()
            if temp==compare:
                ans.append(i)
        return ans
