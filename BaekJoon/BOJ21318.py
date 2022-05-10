from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
count = [0]*(N+1)
for i in range(N-1):
    if nums[i]>nums[i+1]:
        count[i+1] = 1

for i in range(1,N+1):
    count[i]+=count[i-1]

Q = int(stdin.readline())
for _ in range(Q):
    x,y = map(int,stdin.readline().split())
    print(count[y-1]-count[x-1])