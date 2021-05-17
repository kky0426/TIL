from itertools import permutations

def calc(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    
def priority_cal(nums, operation, priority):
    for p in priority:
        idx = 0
        while idx < len(operation):
            if operation[idx] == p:
                temp = calc(int(nums[idx]), int(nums[idx + 1]), operation[idx])
                nums = nums[:idx] + [temp] + nums[idx + 2:]
                operation = operation[:idx] + operation[idx + 1:]
            else:
                idx += 1
    return int(nums[0])
        
                
    
def solution(expression):
    answer = 0
    op=['+','*','-']
    priorities=list(permutations(op,3))
    nums=expression.replace("*"," ").replace("+"," ").replace('-'," ").split()
    
    operation=[]
    for ch in expression:
        if ch in ['-','+','*']:
            operation.append(ch)
    for priority in priorities:
        answer=max(answer,abs(priority_cal(nums,operation,priority)))
    
    return answer
