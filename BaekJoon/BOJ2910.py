from sys import stdin

N,C = map(int,stdin.readline().split())

dic ={}
nums = list(map(int,stdin.readline().split()))

for num in nums:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1

dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
for k,v in dic:
    for _ in range(v):
        print(k,end=" ")
