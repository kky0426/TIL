from sys import stdin
import re

string = stdin.readline().rstrip()
pattern = re.compile(r"(100+1+|01)+")

print("SUBMARINE" if re.fullmatch(pattern,string) else "NOISE")
