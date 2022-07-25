def solution(prices):
    answer = []
    q = deque(prices)
    while q :
        m = q.popleft()
        cnt = 0
        for j in q :
            cnt+= 1
            if m > j :
                break
        answer.append(cnt)
