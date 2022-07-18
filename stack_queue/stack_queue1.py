def solution(progresses, speeds):
    point = 0
    answer = []

    for i in range(100) :
        cnt = 0
        if point == len(progresses) :
            break
        for j in range(len(progresses)) :
            if progresses[j] >= 100 and j == point :
                point += 1
                cnt += 1
            elif progresses[j] < 100 :
                progresses[j] += speeds[j]
        if cnt > 0 :    
            answer.append(cnt)

    return answer
