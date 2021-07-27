from sys import stdin

start=100
ans=0
target=int(stdin.readline())
M= int(stdin.readline())
btn=set(stdin.readline().split())

count = abs(target-start)

for num in range(1000001):
    num=str(num)
    for i in range(len(num)):
        if num[i] in btn:
            break
        elif i==len(num)-1:
            count=min(count,abs(int(num)-target)+len(num))

print(count)
