from sys import stdin

K,L = map(int,stdin.readline().split())
dic = {}


for i in range(L):
    num = stdin.readline().rstrip()
    dic[num] = i

ans = sorted(dic.items(),key=lambda x:x[1])

for num in ans[:K]:
    print(num[0])
