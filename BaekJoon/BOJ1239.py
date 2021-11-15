from sys import stdin

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
ans = 0
def permutation(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next

for candidate in permutation(nums,N):
    for i in range(len(candidate)-1):
        candidate[i+1]+=candidate[i]

    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if candidate[j]-candidate[i] == 50:
                count+=1
                break
    ans = max(ans,count)

print(ans)
