from sys import stdin
from itertools import permutations

N = int(stdin.readline())

lights = [stdin.readline().rstrip() for _ in range(N)]

change = 0
for light in lights:
    change+=light.count("10")
    change+=light.count("01")

ans = float("inf")

for candidate in permutations(lights,N):
    count = 0
    for i in range(N-1):
        if candidate[i][-1] != candidate[i+1][0]:
            count+=1
    ans = min(ans,count+change)

print(ans)
