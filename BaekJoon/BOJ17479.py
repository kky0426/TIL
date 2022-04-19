from sys import stdin

menu = {}

A,B,C = map(int,stdin.readline().split())

for _ in range(A):
    name,price = stdin.readline().split()
    menu[name] = (int(price),"general")

for _ in range(B):
    name,price = stdin.readline().split()
    menu[name] = (int(price),"special")

for _ in range(C):
    name = stdin.readline().rstrip()
    menu[name] = (0,"service")

N = int(stdin.readline())
general = 0
special = 0
service = 0
for _ in range(N):
    order = stdin.readline().rstrip()
    price,category = menu[order]
    if category == "general":
        general+=price
    elif category == "special":
        special+=price
    else:
        service+=1
ans = "Okay"
if service>1:
    ans = "No"

if special>0 and general<20000:
    ans = "No"

if service == 1 and special+general<50000:
    ans = "No"

print(ans)