from collections import deque

def solution(s):
    answer = []
    
    for num in s:
        count = 0
        stack = []
        for ch in num:
            if ch == '0':
                if stack and stack[-2:] == ['1','1']:
                    count+=1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        if count == 0:
            print(count)
            answer.append("".join(stack))
        else:
            res = deque()
            while stack:
                if stack[-1] == '1':
                    res.append(stack.pop())
                else:
                    break
     
            res.appendleft("110"*count)
            answer.append("".join(stack)+"".join(res))
    
        
    return answer
