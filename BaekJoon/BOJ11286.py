from sys import stdin
import heapq

N = int(stdin.readline())

heap = []
for _ in range(N):
    command = int(stdin.readline())

    if command == 0:
        if not heap:
            print(0)
            continue
        pre_abs,pre = heapq.heappop(heap)
        print(pre)

    else:
        heapq.heappush(heap,(abs(command),command))
