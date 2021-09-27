from sys import stdin
import copy

N = int(stdin.readline())

src = list(map(int,stdin.readline().rstrip()))
target = list(map(int,stdin.readline().rstrip()))

def push(src,idx):
    src[idx-1] = 1-src[idx-1]
    src[idx] = 1-src[idx]
    if idx<N-1:
        src[idx+1] = 1-src[idx+1]
    return src

def zero(src):
    src[0] = 1-src[0]
    src[1] = 1-src[1]
    count = 1
    for i in range(1,N):
        if src[i-1] == target[i-1]:
            continue
        else:
            src = push(src,i)
            count+=1
    if src == target:
        return count
    return float("inf")

def non_zero(src):
    count = 0
    for i in range(1,N):
        if src[i-1] == target[i-1]:
            continue
        else:
            src = push(src,i)
            count+=1
    if src == target:
        return count
    return float("inf")

temp = copy.deepcopy(src)
ans = min(zero(src),non_zero(temp))
print(ans if ans!=float("inf") else -1)
