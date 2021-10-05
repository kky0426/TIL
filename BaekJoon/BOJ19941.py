from sys import stdin

N , K = map(int,stdin.readline().split())
ham = list(stdin.readline().rstrip())

ans =0
for i in range(N):
    if ham[i] == 'P':
        for j in range(i-K,i+K+1):
            if 0<=j<N and ham[j] == 'H':
                ans+=1
                ham[j] = '.'
                break

print(ans)
