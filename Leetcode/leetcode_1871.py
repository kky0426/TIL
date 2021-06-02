from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        right=0
        while queue:
            cur = queue.popleft()
            if cur == len(s)-1:
                return True
            
            left= max(cur+minJump,right)
            right = min(cur+maxJump,len(s)-1)
            for i in range(left,right+1):
                if s[i]=='0':
                    queue.append(i)
            
        return False
