class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        ans=0
        left=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            ans=max(ans,right-left+1)
        return ans
