from sys import stdin

def calc(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a//b

string = stdin.readline().rstrip()

stack = []
for ch in string:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(calc(b,a,ch))

print(stack.pop())