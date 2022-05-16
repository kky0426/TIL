from sys import stdin

N,M = map(int,stdin.readline().split())

files = [list(stdin.readline().rstrip().split(".")) for _ in range(N)]

extensions  = {stdin.readline().rstrip() for _ in range(M)}

def in_extensions(ext):
    if ext in extensions:
        return 0
    return 1

files.sort(key=lambda x:(x[0],in_extensions(x[1]),x[1]))

for file in files:
    print(".".join(file))