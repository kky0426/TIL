from sys import stdin

N= int(stdin.readline())

towers=list(map(int,stdin.readline().split()))

stack=[]
ans=[]

for i in range(len(towers)):
    while stack:
        if stack[-1][0]<towers[i]:
            stack.pop()
        else:
            ans.append(stack[-1][1]+1)
            break
    if not stack:
        ans.append(0)
    stack.append((towers[i],i))

for n in ans:
    print(n,end=' ')
