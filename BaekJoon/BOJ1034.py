from sys import stdin

N,M = map(int,stdin.readline().split())
convert = [1,0]
board = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
K = int(stdin.readline())
ans = 0
for i in range(N):
    count = board[i].count(0)
    flag = False
    if count == 0 and K%2 == 0:
        flag = True
    elif K-count == 0:
        flag = True
    elif K-count>0 and (K-count)%2 == 0:
        flag = True

    on = 0
    if flag:
        for j in range(N):
            if board[i] == board[j]:
                on+=1
        ans = max(ans,on)
print(ans)
