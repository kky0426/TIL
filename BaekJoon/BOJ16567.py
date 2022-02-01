from sys import stdin

N,M = map(int,stdin.readline().split())

load = list(map(int,stdin.readline().split()))

def flip(load):
    ans = 0
    flag = False
    for i in range(len(load)):
        if load[i] == 1:
            if not flag:
                flag = True
                ans+=1
        else:
            flag = False
    return ans
count = flip(load)
for _ in range(M):
    line = list(map(int,stdin.readline().split()))
    if line[0] == 0:
        print(count)
    else:
        idx = line[-1]-1
        if load[idx] == 1:
            continue
        load[idx] = load[idx] | 1
        if idx == 0:
            if load[idx+1] == 0:
                count+=1
        elif idx == N-1:
            if load[idx-1] == 0:
                count+=1
        elif load[idx-1] == 0 and load[idx+1] == 0:
            count+=1
        elif load[idx-1] ==1 and load[idx+1] == 1:
            count-=1
