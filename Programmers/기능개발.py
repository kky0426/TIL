from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(speeds)):
        remain = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] == 0:
            queue.append(remain)
        else:
            queue.append(remain+1)
            
    while queue:
        pre = queue.popleft()
        count = 1
        while queue and queue[0]<=pre:
            queue.popleft()
            count+=1
        answer.append(count)
    return answer
