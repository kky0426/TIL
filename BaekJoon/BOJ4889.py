from sys import stdin


idx = 1
while True:
    string = list(stdin.readline().rstrip())
    if '-' in string:
        break
    ans = 0
    stack = []
    for ch in string:
        if ch =='{':
            stack.append(ch)
        else:
            if not stack:
                ans+=1
                stack.append('{')
                continue
            if stack[-1]=='{':
                stack.pop()
    ans+=len(stack)//2
    print("{}. {}".format(idx,ans))
    idx+=1
