from sys import stdin

T = int(stdin.readline())


for _ in range(T):
    a,b,c = map(int,stdin.readline().split())
    ab,bc,ca = map(int,stdin.readline().split())

    ans = 0
    for i in range(min(a,b)+1):
        for j in range(min(b-i,c)+1):
            k = min(a-i,c-j)
            ans = max(ans,ab*i+bc*j+ca*k)
    print(ans)
