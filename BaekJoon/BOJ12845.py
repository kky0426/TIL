from sys import stdin

N = int(stdin.readline())
card = list(map(int,stdin.readline().split()))

ans = 0
max_num = max(card)
ans = max_num*(N-1)+(sum(card)-max_num)
print(ans)
