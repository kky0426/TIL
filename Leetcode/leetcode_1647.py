class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        dic={}
        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        seen = set()
        freq = sorted(dic.values(),reverse=True)
        for i in range(len(freq)):
            while freq[i] in seen:
                freq[i]-=1
                ans+=1
                if freq[i] == 0:
                    break
            seen.add(freq[i])
        return ans
