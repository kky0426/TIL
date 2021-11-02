from sys import stdin

N = int(stdin.readline())
A,B = map(int,stdin.readline().split())
C = int(stdin.readline())
kcal = [int(stdin.readline()) for _ in range(N)]

kcal.sort(reverse=True)

current_price = A
current_kcal = C
for i in range(N):
    if (current_kcal/current_price)>(current_kcal+kcal[i])/(current_price+B):
        break
    current_kcal+=kcal[i]
    current_price+=B

print(int(current_kcal/current_price))
