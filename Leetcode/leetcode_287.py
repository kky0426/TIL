class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        #cycle의 시작점 찾기
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        #중복되는 수 찾기
        fast=nums[0]        
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow
