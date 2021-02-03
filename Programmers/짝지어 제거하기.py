from collections import deque

def solution(s):
    answer = 0
    stack=[]
    deq=deque(s)
    while deq:
        if stack:
            if stack[-1]==deq[0]:
                stack.pop()
                deq.popleft()
            else:
                stack.append(deq.popleft())
        else:
            stack.append(deq.popleft())

    if not stack:
        answer=1
    return answer
