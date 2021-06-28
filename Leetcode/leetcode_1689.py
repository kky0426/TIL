class Solution:
    def minPartitions(self, n: str) -> int:
        ans = list(map(int,list(n)))
        return max(ans)
