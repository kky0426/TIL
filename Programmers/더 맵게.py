import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) < 2 and scoville[0]<K:
            return -1
        fst = heapq.heappop(scoville)
        if fst >= K:
            heapq.heappush(scoville, fst)
            return answer
        else:
            scd = heapq.heappop(scoville)
            mix = fst + scd * 2
            heapq.heappush(scoville, mix)
            answer += 1
