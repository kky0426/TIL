from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    dic = {}
    N = int(stdin.readline())
    for _ in range(N):
        _,category = stdin.readline().split()
        if category in dic:
            dic[category]+=1
        else:
            dic[category]=1

    ans=1
    for _,value in dic.items():
        ans*=value+1
    print(ans-1)
