from sys import stdin

N = int(stdin.readline())
balloons = list(map(int,stdin.readline().split()))
heights = [0]*1000002

ans = 0
for i in range(N):
    heights[balloons[i]]+=1

    if heights[balloons[i]+1] > 0:
        heights[balloons[i]+1]-=1
    else:
        ans+=1

print(ans)