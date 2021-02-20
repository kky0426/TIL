
def solution(numbers):
    answer = ''
    numbers=map(str,numbers)
    numbers=sorted(numbers,key=lambda x:x*3,reverse=True)
    answer=str(int("".join(numbers)))
    return answer
