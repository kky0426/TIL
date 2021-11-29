from sys import stdin

def convert_time(time):
    h = int(time[:2])
    m = int(time[2:])
    return h*60+m

N = int(stdin.readline())

times = []
for _ in range(N):
    s,e = stdin.readline().split()
    times.append((convert_time(s)-10,convert_time(e)+10))
last = convert_time("1000")
ans = 0
times.sort()
for i in range(N):
    if last<times[i][0]:
        ans = max(ans,times[i][0]-last)
    last = max(last,times[i][1])
ans = max(ans,convert_time("2200")-last)
print(ans)
