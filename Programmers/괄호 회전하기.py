def solution(s):
    answer = 0
    N = len(s)

    for i in range(N):
        shift = s[i:]+s[:i]
        if is_right(shift):
            answer+=1
    return answer

def is_right(string):
    stack=[]
    for ch in string:
        if ch in ['[','(','{']:
            stack.append(ch)
        else:
            if not stack:
                return False
            if ch ==']' and stack[-1]=='[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
