from sys import stdin

N = int(stdin.readline())

def compare(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count+=int(ch)
    return count

serial = [stdin.readline().rstrip() for _ in range(N)]

serial.sort(key = lambda x:(len(x),compare(x),x))
for ans in serial:
    print(ans)
