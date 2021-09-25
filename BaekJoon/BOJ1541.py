from sys import stdin

equation = list(stdin.readline().rstrip().split("-"))

ans = []
for i in range(len(equation)):
    ans.append(sum(map(int,equation[i].split('+'))))

answer = ans[0]
for num in ans[1:]:
    answer-=num

print(answer)
