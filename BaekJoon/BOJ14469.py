from sys import stdin

N = int(stdin.readline())

cows=[]
for _ in range(N):
    arv,time = map(int,stdin.readline().split())
    cows.append((arv,time))

cows.sort(key=lambda x:x[0])

current = 0

for arv,time in cows:
    if current<arv:
        current = arv
    current+=time

print(current)
