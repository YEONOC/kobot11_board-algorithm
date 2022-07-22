def solution(arr):

    stack = []
    top = 0
    for i in arr :
        if len(stack) == 0 :
            stack.append(i)
        elif i != stack[top] :
            stack.append(i)
            top += 1
    return stack
