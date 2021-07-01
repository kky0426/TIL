from sys import stdin

N,C = map(int,stdin.readline().split())
home = []

for i in range(N):
    home.append(int(stdin.readline().rstrip()))
home.sort()
left = 1
right = home[-1]-home[0]

while left<=right:
    mid = (left+right)//2
    count = 1
    current = home[0]
    for i in range(1,len(home)):
        if home[i]-current>=mid:
            count+=1
            current = home[i]
    if count<C:
        right = mid-1
    else:
        left = mid+1
print(right)
