from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

ls=len(S)

while len(T)>ls:
    if T[-1]=='A':
        T=T[:-1]
    else:
        T=T[:-1]
        T=T[::-1]

if T==S:
    print(1)
else:
    print(0)
