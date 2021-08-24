from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())

    people = []
    for _ in range(N):
        s,m = map(int,stdin.readline().split())
        people.append((s,m))

    people.sort()
    queue = []
    queue.append(people[0])
    for i in range(1,N):
        if queue[-1][1]>people[i][1]:
            queue.append(people[i])
    print(len(queue))
