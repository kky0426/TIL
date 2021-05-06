from sys import stdin

N=int(stdin.readline())

for _ in range(N):
    password=list(stdin.readline().rstrip())
    left=[]
    right=[]

    for word in password:
        if word=='<':
            if left:
                right.append(left.pop())
        elif word=='>':
            if right:
                left.append(right.pop())
        elif word=='-':
            if left:
                left.pop()
        else:
            left.append(word)

    print("".join(left+right[::-1]))
