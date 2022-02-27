from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    queue = list(map(int,stdin.readline().split()))
    heapq.heapify(queue)
    ans = 1

    while len(queue)>1:
        n1 = heapq.heappop(queue)
        n2 = heapq.heappop(queue)
        ans=ans*n1*n2
        heapq.heappush(queue,n1*n2)
    print(ans%1000000007)
