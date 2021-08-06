from sys import stdin

L,C = map(int,stdin.readline().split())

password = list(stdin.readline().split())
mo = ['a','e','i','o','u']
ans = []
temp=[]

def dfs(temp,password):

    if len(temp) == L:
        count =0
        for ch in mo:
            count+=temp.count(ch)
        if count>0 and L-count>1:
            ans.append("".join(temp))
        return

    for i in range(len(password)):
        temp.append(password[i])
        dfs(temp,password[i+1:])
        temp.pop()

password.sort()
dfs(temp,password)

for string in ans:
    print(string)
