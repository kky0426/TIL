from sys import stdin

def convert_time(time):
    h = time[:2]
    m = time[2:]
    return int(h)*60+int(m)

N = int(stdin.readline())

for scenario in range(N):
    M = int(stdin.readline())
    arr =[]
    for _ in range(M):
        d,s,e = stdin.readline().split()
        arr.append([int(d),convert_time(s),convert_time(e)])
    arr.sort(key=lambda x:(x[0],x[2]))

    ans = 1
    pre = 0
    for i in range(1,M):
        if arr[pre][0]!=arr[i][0] or arr[pre][2] <= arr[i][1]:
            ans+=1
            pre = i
    print("Scenario #{}:".format(scenario+1))
    print(ans)
    print()
