from sys import stdin

N = int(stdin.readline())

permutation = list(map(int,stdin.readline().split()))
flag = False
for i in range(N-1,0,-1):
    if permutation[i-1]<permutation[i]:
        for j in range(N-1,0,-1):
            if permutation[i-1]<permutation[j]:
                permutation[i-1],permutation[j] = permutation[j],permutation[i-1]
                permutation = permutation[:i]+sorted(permutation[i:])
                flag = True
                break
    if flag: break

if flag:
    print(*permutation)
else:
    print(-1)
