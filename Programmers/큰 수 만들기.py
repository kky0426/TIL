def solution(number, k):
    answer = ''
    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack.extend(number[i:])
            break
        stack.append(number[i])
    if k>0:
        for i in range(k):
            stack.pop()
    answer = ''.join(stack)
    return answer
