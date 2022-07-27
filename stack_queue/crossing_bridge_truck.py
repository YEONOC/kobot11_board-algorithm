from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    over = deque([0] * bridge_length)
    sum_over = 0
    while len(over) :
        answer += 1
        k = over.popleft()
        sum_over -= k
        if truck_weights :
            if truck_weights[0] + sum_over <= weight :
                truck = truck_weights.pop(0)
                over.append(truck)
                sum_over += truck
            else :
                over.append(0)
    return answer
