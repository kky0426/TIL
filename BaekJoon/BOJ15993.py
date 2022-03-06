from sys import stdin

T = int(stdin.readline())

odd = [0]*100001
even = [0]*100001

odd[1] = 1
even[2] = 1
odd[2] = 1
odd[3] = 2
even[3] = 2

for i in range(4,100001):
    odd[i] = (even[i-1]+even[i-2]+even[i-3])%1000000009
    even[i] = (odd[i-1]+odd[i-2]+odd[i-3])%1000000009

for _ in range(T):
    N = int(stdin.readline())
    print(odd[N],end=" ")
    print(even[N])

