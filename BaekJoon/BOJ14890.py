from sys import stdin

N,L = map(int,stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(N)]

ans = 0

def check(load):
    slope = [False]*N
    for i in range(N-1):
        if load[i]==load[i+1]:
            continue

        if abs(load[i]-load[i+1])>1:
            return False

        if load[i]>load[i+1]:
            temp = load[i+1]
            for j in range(i+1,i+L+1):
                if j>=N:
                    return False
                if load[j]==temp and not slope[j]:
                    slope[j]=True
                else:
                    return False
        else:
            temp = load[i]
            for j in range(i,i-L,-1):
                if j<0:
                    return False

                if load[j] == temp and not slope[j]:
                    slope[j]=True
                else:
                    return False
    return True

for row in board:
    if check(row):
        ans+=1

for i in range(N):
    temp=[]
    for j in range(N):
        temp.append(board[j][i])
    if check(temp):
        ans+=1

print(ans)
