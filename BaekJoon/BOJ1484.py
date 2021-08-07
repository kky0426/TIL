from sys import stdin

G = int(stdin.readline())

ans = []
start = 1
end = 2

while start<end:
    weigh = end**2 - start**2
    if weigh > G:
        start+=1
    elif weigh < G:
        end+=1
    else:
        ans.append(end)
        end+=1

if ans:
    for a in ans:
        print(a)
else:
    print(-1)
