from sys import stdin

W,H,X,Y,P = map(int,stdin.readline().split())

r = H//2

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2) **(1/2)

def check(x,y):
    if X<=x<=X+W and Y<=y<=Y+H:
        return True

    if distance(x,y,X,Y+r) <= r:
        return True

    if distance(x,y,X+W,Y+r) <= r:
        return True

    return False

ans = 0
for _ in range(P):
    x,y = map(int,stdin.readline().split())
    if check(x,y): ans+=1

print(ans)
