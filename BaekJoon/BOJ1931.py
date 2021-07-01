from sys import stdin

N = int(stdin.readline())
res = []
for _ in range(N):
    temp = list(map(int,stdin.readline().split()))
    res.append(temp)

res = sorted(res,key=lambda x:(x[1],x[0]))
ans = []
for i in range(len(res)):
    if ans:
        if ans[-1][1]<=res[i][0]:
            ans.append(res[i])
    else:
        ans.append(res[i])
print(len(ans))

