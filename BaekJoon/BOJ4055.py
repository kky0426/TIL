from sys import stdin

day = 1
def convert(time):
    time = int(time)
    return (time-8)*2

def best_index(t,np,arr):
    idx = -1
    best = 33
    for i in range(np):
        if t>=arr[i][0] and t<arr[i][1] and arr[i][1]<best:
            idx = i
            best = arr[i][1]
    return idx

while True:
    N = int(stdin.readline())
    if N == 0:
        break

    parties = [list(map(convert,stdin.readline().split())) for _ in range(N)]
    count = 0
    for i in range(32):
        idx = best_index(i,N,parties)
        if idx>=0:
            count+=1
            parties[idx][0] = 32


    print("On day {} Emma can attend as many as {} parties.".format(day,count))
    day+=1
