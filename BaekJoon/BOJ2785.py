from sys import stdin

N = int(stdin.readline())
chains = list(map(int,stdin.readline().split()))
chains.sort()

count = 1
for chain in chains:
    if count+chain >= N:
        break
    else:
        count+=chain
        N-=1

print(N-1)
