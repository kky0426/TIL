from sys import stdin

N=int(stdin.readline())
people=[]
ans=[0]*N

for _ in range(N):
    w,h=map(int,stdin.readline().split())
    people.append((w,h))

for i in range(N):
    count=0
    for j in range(N):
        if i==j:
            continue
        if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            count+=1
    ans[i]=count+1

for i in ans:
    print(i,end=" ")
