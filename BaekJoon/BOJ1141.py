from sys import stdin

N = int(stdin.readline())

strings = [stdin.readline().rstrip() for _ in range(N)]
strings.sort()

ans = []
for i in range(N-1):
    for j in range(i+1,N):
        if strings[j].startswith(strings[i]):
            ans.append(strings[i])
            break

print(N-len(ans))
