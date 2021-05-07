from sys import stdin


N=int(stdin.readline().rstrip())
mem=[0]*N  # 현재 row에 대한 col 값을 저장
visit=[False]*N
def back(row,col):
    #가지치기
    for i in range(row):
        # column이 같은경우
        if col==mem[i]:
            return 0
        # 대각선
        if (row-i)-abs(col-mem[i])==0:
            return 0

    #종료조건 (맨끝열에 체스말을 둘 경우)
    if row==N-1:
        return 1

    mem[row]=col

    count=0
    for i in range(N):
        if visit[i]: continue

        visit[i] = True
        count+=back(row+1,i)
        visit[i] = False
    return count

ans=0

for i in range(N):
    ans+=back(0,i)
print(ans)
