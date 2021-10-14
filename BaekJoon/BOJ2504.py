from sys import stdin,exit

bracket = stdin.readline().rstrip()

stack = []
for ch in bracket:
    if ch == ')':
        if not stack:
            print(0)
            exit(0)
        num = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if num == 0:
                    stack.append(2)
                else:
                    stack.append(2*num)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                if num == 0:
                    num = top
                else:
                    num = num+top

    elif ch == ']':
        num = 0
        if not stack:
            print(0)
            exit(0)
        while stack:
            top = stack.pop()
            if top == '[':
                if num == 0:
                    stack.append(3)
                else:
                    stack.append(num*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                if num == 0:
                    num = top
                else:
                    num = num+top

    else:
        stack.append(ch)

ans = 0

for n in stack:
    if n == '(' or n == '[':
        print(0)
        exit(0)
    else:
        ans+=n

print(ans)
