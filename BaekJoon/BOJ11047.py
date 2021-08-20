from sys import stdin

N,K = map(int,stdin.readline().split())

coin=[]
for _ in range(N):
    coin.append(int(stdin.readline()))

coin.sort(reverse=True)

ans = 0
while K>0:
    for c in coin:
        if K>=c:
            temp = K//c
            ans+=temp
            K-=temp*c
            break
print(ans)
