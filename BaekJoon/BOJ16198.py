from sys import stdin

N = int(stdin.readline())

energy = list(map(int,stdin.readline().split()))

ans = 0

def solve(n,eng,s):
    if n == 2:
        global ans
        ans = max(ans,s)
        return
    for i in range(1,len(eng)-1):
        solve(n-1,eng[:i]+eng[i+1:],s+eng[i-1]*eng[i+1])

solve(N,energy,0)
print(ans)
