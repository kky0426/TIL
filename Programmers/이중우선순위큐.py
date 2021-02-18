import heapq


def solution(operations):


    heap = []
    heapq.heapify(heap)
    answer = []
    for com in operations:
        if com == 'D 1':
            if heap:
                heap.pop(heap.index(max(heap)))

        elif com == 'D -1':
            if heap:
                heapq.heappop(heap)
        else:
            temp, num = com.split()
            heapq.heappush(heap, int(num))
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer=[0,0]
    return answer
