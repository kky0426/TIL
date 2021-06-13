class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        count_one = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_one+=1
        
        if abs(2*count_one - len(s)) > 1:
            return -1
        
        if len(s) > 2*count_one:
            temp=""
            for i in range(len(s)):
                if i%2 == 0:
                    temp+='0'
                else:
                    temp+='1'
            for j in range(len(temp)):
                if temp[j]!=s[j]:
                    ans+=1
        elif len(s) < 2*count_one:
            temp=""
            for i in range(len(s)):
                if i%2 == 0:
                    temp+='1'
                else:
                    temp+='0'
            for j in range(len(temp)):
                if temp[j]!=s[j]:
                    ans+=1
        else:
            temp=""
            temp2=""
            ans2=0
            for i in range(len(s)):
                if i%2 == 0:
                    temp+='0'
                    temp2+='1'
                else:
                    temp+='1'
                    temp2+='0'
            for j in range(len(temp)):
                if temp[j]!=s[j]:
                    ans+=1
                if temp2[j]!=s[j]:
                    ans2+=1
            ans = min(ans,ans2)
           
        return ans//2
