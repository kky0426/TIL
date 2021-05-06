from sys import stdin
import heapq
N=int(stdin.readline())

max_heap=[]
min_heap=[]

for i in range(N):
    num=int(stdin.readline())
    if len(max_heap)==len(min_heap):
        heapq.heappush(max_heap,(-num,num))
    else:
        heapq.heappush(min_heap,(num,num))

    if max_heap and min_heap and max_heap[0][1]>min_heap[0][1]:
        min_num=heapq.heappop(min_heap)[1]
        max_num=heapq.heappop(max_heap)[1]
        heapq.heappush(max_heap,(-min_num,min_num))
        heapq.heappush(min_heap,(max_num,max_num))
    print(max_heap[0][1])
