from sys import stdin

def permutation(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next


N = int(stdin.readline())
idx = [i for i in range(N)]
board = [list(map(int,stdin.readline().split())) for _ in range(N)]

ans = float("inf")
for candidate in permutation(idx,N):
    weight = 0
    flag = True
    for i in range(N-1):
        if board[candidate[i]][candidate[i+1]]>0:
            weight+=board[candidate[i]][candidate[i+1]]
        else:
            flag=False
            break
    if board[candidate[-1]][candidate[0]]>0:
        weight+=board[candidate[-1]][candidate[0]]
    else:
        flag=False
        
    if flag: ans = min(ans,weight)

print(ans)
