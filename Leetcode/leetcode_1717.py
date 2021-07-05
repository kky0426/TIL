class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s)<2:
            return 0
        
        ans = 0
        stack = []
        
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>=2:
                if x>=y and stack[-2]+stack[-1] == 'ab':
                    ans+=x
                    stack.pop()
                    stack.pop()
                elif x<y and stack[-2]+stack[-1] == 'ba':
                    ans+=y
                    stack.pop()
                    stack.pop()
                    
        s = "".join(stack)
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>=2:
                if x>=y and stack[-2]+stack[-1] == 'ba':
                    ans+=y
                    stack.pop()
                    stack.pop()
                elif x<y and stack[-2]+stack[-1] == 'ab':
                    ans+=x
                    stack.pop()
                    stack.pop()
        return ans
