import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dic = collections.defaultdict(list)
        #visit = [[0]*10 for _ in range(n)]
        ans = 0
        for r,c in reservedSeats:
            dic[r-1].append(c-1)
            

            
        for k,v in dic.items():
            if len(v)==0:
                ans+=2
            elif v in [0,9]:
                ans+=2
            else:
                visit = [0]*10
                for j in v:
                    visit[j]=1
                count = 0
                if visit[1:5] == [0,0,0,0]:
                    count+=1
                if visit[5:9] == [0,0,0,0]:
                    count+=1
                if count==0 and visit[3:7]==[0,0,0,0]:
                    count+=1
                ans+=count
                
        ans += 2*(n-len(dic))
        return ans
