from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        queue = deque()
        start,end=0,0
        while end<len(nums):
            # queue[0]을 max 값 으로 유지
            while queue and nums[end]>queue[-1]:
                queue.pop()
            queue.append(nums[end])
            
            # window 만큼 검사 
            if end-start+1 == k:
                ans.append(queue[0])
                
                #max값이 window의 처음 값이면 pop
                if queue[0] == nums[start]:
                    queue.popleft()
                start+=1
            
            end+=1

        return ans
