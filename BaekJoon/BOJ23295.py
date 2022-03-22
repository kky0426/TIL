from sys import stdin

N,T = map(int,stdin.readline().split())

time = [0]*100001
arr = [0]*100001

for _ in range(N):
    K = int(stdin.readline())
    for _ in range(K):
        s,e = map(int,stdin.readline().split())
        time[s]+=1
        time[e]-=1

for i in range(1,100001):
    time[i]+=time[i-1]

arr[0] = time[0]
for i in range(1,100001):
    arr[i]+=arr[i-1]+time[i]

start = 0
end = T
count = arr[T-1]

for i in range(1,100001-T):
    if count<arr[i+T-1]-arr[i-1]:
        start = i
        end = i+T
        count = arr[i+T-1]-arr[i-1]

print(start,end)