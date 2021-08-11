from sys import stdin

N = int(stdin.readline())

string = set()
for _ in range(N):
    string.add(stdin.readline().rstrip())

string = sorted(string,key=lambda x:(len(x),x))
for ans in string:
    print(ans)
