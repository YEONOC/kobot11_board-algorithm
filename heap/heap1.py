import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K :
        if len(scoville) == 1:
            answer = -1
            break
        mins = heapq.heappop(scoville)
        mins2 = heapq.heappop(scoville)
        heapq.heappush(scoville, mins+(mins2*2))
        answer += 1
    return answer
