from sys import stdin
import bisect

T = int(stdin.readline())

for t in range(T):
    N,K = map(int,stdin.readline().split())
    stocks = list(map(int,stdin.readline().split()))

    queue = []
    queue.append(stocks[0])

    for i in range(1,N):
        if stocks[i]>queue[-1]:
            queue.append(stocks[i])
        else:
            idx = bisect.bisect_left(queue,stocks[i])
            queue[idx] = stocks[i]

    print("Case #{}".format(t+1))
    if len(queue)>=K:
        print(1)
    else:
        print(0)