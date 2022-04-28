from sys import stdin


while True:
    N,M = map(float,stdin.readline().split())
    if N == 0 and M == 0:
        break
    N = int(N)
    M = int(M*100)

    candy = []
    for _ in range(N):
        kcal,price = map(float,stdin.readline().split())
        candy.append((int(kcal),int(price*100+0.5)))

    dp = [0]*100001

    for i in range(1,M+1):
        for c,p in candy:
            if i-p>=0:
                dp[i] = max(dp[i],dp[i-p]+c)
    print(dp[M])