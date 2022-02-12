from sys import stdin
import bisect

N = int(stdin.readline())

line = [list(map(int,stdin.readline().split())) for _ in range(N)]
dic={}
for i in range(N):
    dic[line[i][1]] = line[i][0]

line.sort(key=lambda x:x[0])

lis = []
trace = [0]*N
length = 0
for i in range(N):
    num = line[i][1]
    idx = bisect.bisect_left(lis,num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num
    trace[i] = idx+1

result = []
length = len(lis)
print(N-length)
for i in range(len(trace)-1,-1,-1):
    if trace[i] == length:
        length-=1
    else:
        result.append(line[i][0])

for n in result[::-1]:
    print(n)
