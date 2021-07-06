from sys import stdin

string = list(stdin.readline().rstrip())
boom = list(stdin.readline().rstrip())

stack = []

for ch in string:
    stack.append(ch)
    if len(stack)>=len(boom):

        if stack[len(stack)-len(boom):len(stack)] == boom:
            for _ in range(len(boom)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")
