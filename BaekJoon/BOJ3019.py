from sys import stdin

C,P = map(int,stdin.readline().split())
field = list(map(int,stdin.readline().split()))

ans = 0

if P == 1:
    ans+=C
    for i in range(C-3):
        if field[i] == field[i+1] and field[i+1]==field[i+2] and field[i+2] == field[i+3]:
            ans+=1
elif P == 2:
    for i in range(C-1):
        if field[i]==field[i+1]:
            ans+=1
elif P == 3:
    for i in range(C-2):
        if field[i]==field[i+1] and field[i+1]==field[i+2]-1:
            ans+=1
    for i in range(C-1):
        if field[i]-1 == field[i+1]:
            ans+=1
elif P==4:
    for i in range(C-2):
        if field[i]==field[i+1]+1 and field[i+1] == field[i+2]:
            ans+=1
    for i in range(C-1):
        if field[i]+1 == field[i+1]:
            ans+=1

elif P==5:
    for i in range(C-2):
        if field[i] == field[i+1] and field[i+1] == field[i+2]:
            ans+=1

    for i in range(C-1):
        if field[i]-1 == field[i+1]:
            ans+=1

    for i in range(C-1):
        if field[i]+1 == field[i+1]:
            ans+=1

    for i in range(C-2):
        if field[i] == field[i+1]+1 and field[i+1]+1 == field[i+2]:
            ans+=1

elif P == 6:
    for i in range(C-2):
        if field[i] == field[i+1] and field[i+1] == field[i+2]:
            ans+=1
        if field[i]==field[i+1]-1 and field[i+1]==field[i+2]:
            ans+=1

    for i in range(C-1):
        if field[i] == field[i+1]:
            ans+=1
        if field[i]==field[i+1]+2:
            ans+=1

elif P == 7:
    for i in range(C - 2):
        if field[i] == field[i + 1] and field[i + 1] == field[i + 2]:
            ans += 1
        if field[i] == field[i + 1]  and field[i + 1] == field[i + 2]+1:
            ans += 1

    for i in range(C - 1):
        if field[i] == field[i + 1]:
            ans += 1
        if field[i] == field[i + 1] - 2:
            ans += 1

print(ans)
