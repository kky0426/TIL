from sys import stdin

N = int(stdin.readline())
people = list(map(int,stdin.readline().split()))

minus = 0
plus = 0
people.sort(reverse=True)
count = 0
for num in people:
    if num<0:
        minus+=num
    else:
        plus+=num
        count+=1

ans = plus*count+minus

for i in range(N):
    if people[i]>=0:
        continue
    plus+=people[i]
    minus-=people[i]
    count+=1
    ans = max(ans,plus*count+minus)

print(ans)
