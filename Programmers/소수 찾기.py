from itertools import permutations

def is_prime(num):
    if num <2:
        return False
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidates = []
    for i in range(1,len(numbers)+1):
        candidates += list(permutations(numbers,i))
    
    num_set = set()
    for num in list(set(candidates)):
        num_set.add(int("".join(num)))
    
    for num in num_set:
        if is_prime(num):
            answer+=1


    return answer
