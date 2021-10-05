from sys import stdin

N = int(stdin.readline())

in_car  = [stdin.readline().rstrip() for _ in range(N)]
out_car = [stdin.readline().rstrip() for _ in range(N)]

dic = {}
for i in range(N):
    dic[in_car[i]] = i

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        if dic[out_car[i]] > dic[out_car[j]]:
            ans+=1
            break
print(ans)
