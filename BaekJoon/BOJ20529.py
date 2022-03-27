from sys import stdin

def dfs(idx,depth):
    if depth == 3:
        global ans
        ans = min(ans,get_dis(out[0],out[1])+get_dis(out[1],out[2])+get_dis(out[0],out[2]))
        return

    for i in range(idx+1,N):
        out.append(arr[i])
        dfs(i,depth+1)
        out.pop()

def get_dis(x,y):
    count = 0
    for i in range(4):
        if x[i]!=y[i]:
            count+=1
    return count

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    arr = list(stdin.readline().split())
    if N>32:
        print(0)
    else:
        out = []
        ans = float("inf")
        dfs(-1,0)
        print(ans)
