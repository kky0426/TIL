def solution(price, money, count):
    ans = 0
    for i in range(1,count+1):
        ans+=price*i
    ans -=money
    return ans if ans>0 else 0
