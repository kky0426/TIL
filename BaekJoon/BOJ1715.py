from sys import stdin
import heapq

N = int(stdin.readline())
card=[]
for _ in range(N):
    heapq.heappush(card,int(stdin.readline()))

ans=0
l=len(card)
while l>1:
    compare = heapq.heappop(card)+heapq.heappop(card)
    ans+=compare
    heapq.heappush(card,compare)
    l-=1
print(ans)
