from sys import stdin
import re

T = int(stdin.readline())
pattern = re.compile(r"(100+1+|01)+")
for _ in range(T):
    string = stdin.readline().rstrip()
    if re.fullmatch(pattern,string):
        print("YES")
    else:
        print("NO")
