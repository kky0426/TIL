def convert_number(num,n):
    temp = ""
    while num>0:
        mod = num%n
        num = num//n
        temp+=str(mod)
    return temp[::-1]

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n_digit = convert_number(n,k)
    nums = n_digit.split("0")

    for num in nums:
        if num == '':
            continue
        if is_prime(int(num)):
            answer+=1
    return answer
