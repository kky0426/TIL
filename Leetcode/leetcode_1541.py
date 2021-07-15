class Solution:
    def minInsertions(self, s: str) -> int:
        ans=0
        stack=[]
        s=s.replace("))","}")
        print(s)
        for ch in s:
            if ch=='(':
                stack.append(ch)
            elif ch=='}':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    ans+=1
            else:
                if stack and stack[-1]=='(':
                    ans+=1
                    stack.pop()
                else:
                    ans+=2
               
        ans+=2*len(stack)
        return ans
