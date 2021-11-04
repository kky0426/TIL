from sys import stdin

T = int(stdin.readline())

while T>0:
    N = int(stdin.readline())
    stock = list(map(int,stdin.readline().split()))
    ans = 0
    max_value = 0
    for i in range(N-1,-1,-1):
        if max_value <= stock[i]:
            max_value = stock[i]
        else:
            ans+=max_value-stock[i]
    print(ans)
    T-=1
