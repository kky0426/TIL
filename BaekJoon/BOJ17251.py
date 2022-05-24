from sys import stdin

N = int(stdin.readline())
power = list(map(int,stdin.readline().split()))

left = [0]*N
right = [0]*N

left[0] = power[0]
pre = left[0]
for i in range(1,N):
    if pre>power[i]:
        left[i] = pre
    else:
        left[i] = power[i]
        pre = left[i]

right[-1] = power[-1]
pre = right[-1]
for i in range(N-2,-1,-1):
    if pre>power[i]:
        right[i] = pre
    else:
        right[i] = power[i]
        pre = right[i]

red = 0
blue = 0

for i in range(N-1):
    if left[i] > right[i+1]:
        red+=1
    elif left[i]<right[i+1]:
        blue+=1

if red>blue:
    print("R")
elif red<blue:
    print("B")
else:
    print("X")
