from sys import stdin

N,M = map(int,stdin.readline().split())

books = list(map(int,stdin.readline().split()))
pos = []
neg = []

for book in books:
    if book>0:
        pos.append(book)
    else:
        neg.append(book)

pos.sort(reverse=True)
neg.sort()

distance = []
for i in range(0,len(pos),M):
    temp = pos[i:i+M]
    dis = max(map(abs,temp))
    distance.append(dis)

for i in range(0,len(neg),M):
    temp = neg[i:i+M]
    dis = max(map(abs,temp))
    distance.append(dis)

distance.sort()
ans = distance.pop()
ans+= 2*sum(distance)
print(ans)
