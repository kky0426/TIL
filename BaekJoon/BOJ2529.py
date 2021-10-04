from sys import stdin

N = int(stdin.readline())
bracket = list(stdin.readline().rstrip().split())

def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j

max_ans = ""
min_ans = ""

visit = [False]*10

def dfs(idx,string):
    global max_ans,min_ans
    if idx == N+1:
        if len(min_ans)==0:
            min_ans = string
        else:
            max_ans = string
        return

    for i in range(10):
        if not visit[i]:
            if idx == 0 or check(string[-1],str(i),bracket[idx-1]):
                visit[i]=True
                dfs(idx+1,string+str(i))
                visit[i]=False

dfs(0,"")
print(max_ans)
print(min_ans)
