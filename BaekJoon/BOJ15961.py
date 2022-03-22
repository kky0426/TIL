from sys import stdin
from collections import deque

N,d,k,c = map(int,stdin.readline().split())

sushi = [int(stdin.readline()) for _ in range(N)]

count = [0]*(d+1)

for i in range(k):
    sushi.append(sushi[i])

queue = deque()
ans = 0

for i in range(k):
    queue.append(sushi[i])
    if count[sushi[i]] == 0:
        ans+=1
    count[sushi[i]]+=1

kind = ans
for i in range(k,N+k):
    rm = queue.popleft()
    count[rm]-=1
    if count[rm] == 0:
        kind-=1

    if count[sushi[i]] == 0:
        kind+=1
    count[sushi[i]]+=1
    queue.append(sushi[i])

    if count[c] == 0:
        ans = max(ans,kind+1)
    else:
        ans = max(ans,kind)

print(ans)

