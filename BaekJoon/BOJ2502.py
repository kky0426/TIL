from sys import stdin

N,M = map(int,stdin.readline().split())

def dfs(day,fst,scd):
    if day == 0:
        dp[0] = fst
        return dp[0]

    if day == 1:
        dp[1] = scd
        return dp[1]

    if dp[day]!=0:
        return dp[day]


    dp[day] = dfs(day-1,fst,scd)+dfs(day-2,fst,scd)
    return dp[day]
first = 1
second = 1

while True:
    dp = [0 for _ in range(N)]
    dfs(N-1,first,second)
    if dp[-1]>M:
        first+=1
        second=first
    elif dp[-1]<M:
        second+=1
    else:
        print(first,second,sep="\n")
        break
