from sys import stdin

left_stack = list(stdin.readline().rstrip())
right_stack = []

M = int(stdin.readline())

for _ in range(M):
    command = stdin.readline().rstrip()
    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command =='B':
        if left_stack:
            left_stack.pop()
    else:
        _,ch =command.split()
        left_stack.append(ch)

print("".join(left_stack+list(reversed(right_stack))))
