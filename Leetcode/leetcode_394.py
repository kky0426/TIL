class Solution:
    def decodeString(self, s: str) -> str:
        string=""
        nums=[]
        stack=[]
        stack.append("")
        for i in range(len(s)):
            if s[i].isdigit():
                if i>0 and s[i-1].isdigit():
                    nums[-1]+=s[i]
                else:    
                    nums.append(s[i])
            elif s[i].isalpha():
                string+=s[i]
            elif s[i]=='[':
                stack.append(string)
                string=""
            elif s[i]==']':
                n=int(nums.pop())
                string*=n
                string=stack.pop()+string
        return string
