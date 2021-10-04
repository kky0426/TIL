from sys import stdin

N,M = map(int,stdin.readline().split())

def gcd(x,y):
    if y == 0: return x
    else: return gcd(y,x%y)

print(M-gcd(N,M))
