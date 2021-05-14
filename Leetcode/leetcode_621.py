from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        dic={}
        for i in range(len(tasks)):
            if tasks[i] in dic:
                dic[tasks[i]]+=1
            else:
                dic[tasks[i]]=1
        sdic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        ans=[0]*(n)*sdic[0][1]
        
        off=0
        for ch,num in sdic:
            idx=off
            while num>0:
                if idx>=len(ans):
                    for _ in range(n+1):
                        ans.append(0)
                ans[idx]=ch
                idx+=n+1
                num-=1
            off+=1
        while ans[-1]==0:
            ans.pop()
        return max(len(ans),len(tasks))
