from sys import stdin

string = stdin.readline().rstrip()

dic = {'H':1,'C':12,'O':16}
stack = []

for ch in string:
    if ch in dic:
        stack.append(dic[ch])
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        count = 0
        while True:
            temp=stack.pop()
            if temp == '(':
                break
            count+=temp

        if count == 0:
            continue
        else:
            stack.append(count)
    else:
        stack.append(stack.pop()*int(ch))

print(sum(stack))
