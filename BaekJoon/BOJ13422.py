from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N,M,K = map(int,stdin.readline().split())
    house = list(map(int,stdin.readline().split()))
    house = house*2
    ans = 0
    s = 0
    count = 0
    for i in range(N+M-1):
        s+=house[i]
        count+=1

        if count<M:
            continue

        if s<K:
            ans+=1
        count-=1
        s-=house[i-M+1]
        
        if N == M:
            break
    print(ans)
