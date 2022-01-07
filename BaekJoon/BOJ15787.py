from sys import stdin

N,M = map(int,stdin.readline().split())

commands = [list(map(int,stdin.readline().split())) for _ in range(M)]


train = [0]*N

for command in commands:
    c = command[0]
    i = command[1]-1
    if len(command)==3: x = command[2]-1

    if c == 1:
        train[i] = train[i] | (1<<x)
    elif c == 2:
        train[i] = train[i] & ~(1<<x)
    elif c == 3:
        train[i] = (train[i]<<1) & ~(2**20)
    else:
        train[i] = train[i]>>1

print(len(set(train)))
