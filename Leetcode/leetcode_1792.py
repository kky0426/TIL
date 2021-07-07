import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ans = 0
        heap = []
        for p,t in classes:
            origin = p/t
            add = (p+1)/(t+1)
            diff = add-origin
            heapq.heappush(heap,(-diff,p,t))
        
        while extraStudents>0:
            _,p,t = heapq.heappop(heap)
            p+=1
            t+=1
            diff = (p+1)/(t+1)-p/t
            heapq.heappush(heap,(-diff,p,t))
            extraStudents-=1
            
        for _,i,k in heap:
            ans+=i/k
            
        return ans/len(classes)
