from sys import stdin

D,N = map(int,stdin.readline().split())

oven = list(map(int,stdin.readline().split()))

for i in range(1,D):
    if oven[i-1]<oven[i]:
        oven[i] = oven[i-1]

pizza = list(map(int,stdin.readline().split()))

depth = D-1
count = 0
flag = False
for i in range(D-1,-1,-1):
    if count == len(pizza):
        flag = True
        break

    if oven[i]>=pizza[count]:
        count+=1
        depth = i

print(depth+1) if flag else print(0)
