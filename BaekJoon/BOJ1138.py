from sys import stdin

N = int(stdin.readline())

people = list(map(int,stdin.readline().split()))
arr = [(people[i],i+1) for i in range(N)]
arr.sort(key=lambda x:x[1],reverse=True)

ans = []
for idx,height in arr:
    ans.insert(idx,height)
print(*ans)
