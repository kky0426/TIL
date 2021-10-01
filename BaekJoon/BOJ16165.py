from sys import stdin
from collections import defaultdict
N,M = map(int,stdin.readline().split())

team = defaultdict(list)
member={}
for _ in range(N):
    team_name = stdin.readline().rstrip()
    k = int(stdin.readline())
    for _ in range(k):
        member_name = stdin.readline().rstrip()
        team[team_name].append(member_name)
        member[member_name] = team_name

for _ in range(M):
    q = stdin.readline().rstrip()
    n = int(stdin.readline())
    if n == 1:
        print(member[q])
    else:
        for name in sorted(team[q]):
            print(name)
