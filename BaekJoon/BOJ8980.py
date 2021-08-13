from sys import stdin

N,C = map(int,stdin.readline().split())

M = int(stdin.readline())

boxes = []
for _ in range(M):
    s,e,w = map(int,stdin.readline().split())
    boxes.append((s,e,w))

boxes.sort(key = lambda x:x[1])

capacity = [C]*(N+1)
ans = 0
for box in boxes:
    start,end,value = box[0],box[1],box[2]
    min_cap = min(min(capacity[start:end]),value)
    for i in range(start,end):
        capacity[i]-=min_cap
    ans += min_cap

print(ans)
