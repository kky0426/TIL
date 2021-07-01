from sys import stdin
K,N = map(int,stdin.readline().split())
lan = []

for _ in range(K):
    lan.append(int(stdin.readline().rstrip()))

left = 1
right = max(lan)

while left<=right:
    mid = (left+right)//2
    count = 0
    for i in range(len(lan)):
        count+=lan[i]//mid
    if count<N:
        right = mid-1
    else:
        left = mid+1

print(right)
