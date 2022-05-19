from sys import stdin

string = stdin.readline().rstrip()

ans = 0
k=0
p=0

for ch in string:
    if ch == "K":
        k+=1
        if p-1<0:
            p = 0
            ans+=1
        else:
            p-=1
    else:
        p+=1
        if k-1<0:
            k=0
            ans+=1
        else:
            k-=1

print(ans)