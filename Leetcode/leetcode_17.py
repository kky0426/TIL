class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        word={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
             '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        if len(digits)==0:
            return ans
        #current 에 하나씩 추가 idx=digits의 인덱스
        def dfs(current,idx):
            if len(current)==len(digits):
                ans.append(current)
                return
            
            for ch in word[digits[idx]]:
                dfs(current+ch,idx+1)
        dfs("",0)
        return ans
