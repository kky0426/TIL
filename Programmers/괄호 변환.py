def is_balanced(s):
    if s.count('(') == s.count(')'):
        return True
    else:
        return False

def is_right(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        elif s[i]==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(s[i])

    if stack:
        return False
    else:
        return True
    
def devide(s):
    u=''
    for i in range(len(s)):
        u+=s[i]
        if is_balanced(u):
            v=s[i+1:]
            return u,v
        
def solution(p):
    answer = ''
    if p=='':
        return ''
    
    if is_right(p):
        return p
    
    u,v=devide(p)
    
    if is_right(u):
        return u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        temp=u[1:-1]
        for i in range(len(temp)):
            if temp[i]=='(':
                answer+=')'
            else:
                answer+='('
        return answer
