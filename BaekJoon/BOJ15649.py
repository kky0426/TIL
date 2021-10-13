from sys import stdin

N,M = map(int,stdin.readline().split())

arr = [i for i in range(1,N+1)]

def permutations(arr,n):
    for i in range(len(arr)):
        if n==1:
            yield [arr[i]]
        else:
            for next in permutations(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next

for nums in permutations(arr,M):
    print(" ".join(map(str,nums)))
