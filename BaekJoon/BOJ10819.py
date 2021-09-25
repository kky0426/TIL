from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

def permutation(arr,n):
    for i in range(len(arr)):
        if n==1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next
ans = 0
for candidate in permutation(nums,N):
    count= 0
    for i in range(N-1):
        count+=abs(candidate[i]-candidate[i+1])

    ans = max(ans,count)

print(ans)
