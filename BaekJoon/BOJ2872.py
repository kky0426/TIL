from sys import stdin

N = int(stdin.readline())

book = [int(stdin.readline()) for _ in range(N)]

ans = 0
idx = N
for i in range(N-1,-1,-1):
    if book[i] == idx:
        idx-=1
    else:
        ans+=1

print(ans)
