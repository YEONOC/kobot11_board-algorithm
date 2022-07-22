def solution(n, lost, reserve):
    answer = n - len(lost)
    lost = sorted(lost)
    reserve = sorted(reserve)
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if lost[i] == reserve[j] : # 도난 당했는데 여벌 있음
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if abs(lost[i]-reserve[j]) == 1 and lost[i] > 0 and reserve[j] > 0 : 
            # 도난당했는데 앞 뒤 번호중에 여벌옷 있음
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break
    return answer
