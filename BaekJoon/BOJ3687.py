from sys import stdin

def get_max(num):
    if num % 2 == 0:
        ans = "1" * (num // 2)
    else:
        ans = "7" + "1" * ((num - 3) // 2)
    return ans

def get_min(num):
    if num%7 == 0:
        return "8"*(num//7)
    elif num%7 == 1:
        return "10" + "8"*((num//7)-1)
    elif num%7 == 2:
        return "1" + "8"*(num//7)
    elif num%7 == 3:
        if num<7:
            return "7"
        if num<=10:
            return "22"
        return "200"+"8"*((num//7)-2)
    elif num%7 == 4:
        if num<7:
            return "4"
        return "20"+"8"*((num//7)-1)
    elif num%7 == 5:
        return "2"+"8"*(num//7)
    elif num%7 == 6:
        return "6"+"8"*(num//7)

T = int(stdin.readline())
for i in range(T):
    num = int(stdin.readline())
    print(get_min(num),get_max(num))
