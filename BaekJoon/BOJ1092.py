from sys import stdin
import sys

N = int(stdin.readline())
tower = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
box=list(map(int,stdin.readline().split()))
tower.sort(reverse=True)
box.sort(reverse=True)

time = 0
start = 0
if tower[0]<box[0]:
    print(-1)
    sys.exit(0)

while box:
    time +=1
    for w in tower:
        for i in range(len(box)):
            if box and box[i]<=w:
                del box[i]
                break
print(time)
