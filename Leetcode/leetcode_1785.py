class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        ans = 0
        S = sum(nums)
        sub = S-goal
        count = abs(sub/limit)
        if count == int(count):
            ans = int(count)
        else:
            ans = int(count)+1
        return ans
