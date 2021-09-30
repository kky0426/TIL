from sys import stdin

N,S = map(int,stdin.readline().split())
spot = list(map(int,stdin.readline().split()))

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

diff = [abs(S-i) for i in spot]
ans = min(diff)
for i in diff:
    ans = gcd(ans,i)

print(ans)
