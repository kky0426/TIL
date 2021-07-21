from sys import stdin

people = []
for _ in range(9):
    people.append(int(stdin.readline()))

total=sum(people)
for i in range(8):
    for j in range(i+1,9):
        if total-people[i]-people[j]==100:
            ans=people[:i]+people[i+1:j]+people[j+1:]
            break
ans.sort()
for p in ans:
    print(p)
