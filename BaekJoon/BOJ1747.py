from sys import stdin

N = int(stdin.readline())
MAX = 1003001
prime = [True for _ in range(MAX+1)]

for i in range(2,int(MAX**(1/2))+1):
    if prime[i]:
        j = 2
        while i*j<=MAX:
            prime[i*j] = False
            j+=1

def is_pallendrome(num):
    num = str(num)
    l = len(num)
    left = 0
    right = l-1
    while left<=right:
        if num[left]!=num[right]:
            return False
        left+=1
        right-=1
    return True

N = max(N,2)
for i in range(N,MAX+1):
    if prime[i] and is_pallendrome(i):
        print(i)
        break
