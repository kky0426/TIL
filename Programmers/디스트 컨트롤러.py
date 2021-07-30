import heapq
from collections import deque

def solution(jobs):
    N=len(jobs)
    jobs.sort(key=lambda x:x[0])
    jobs=deque(jobs)
    queue=[(0,0)]
    answer=0
    current=0
    while jobs or queue:
        while jobs:
            if jobs[0][0]<=current:
                heapq.heappush(queue,(jobs[0][1],jobs[0][0]))
                jobs.popleft()
            else:
                break
        
        if queue:
            time,start = heapq.heappop(queue)
            answer+=time+current-start
            current+=time
        else:
            current+=1
    return int(answer/N)
