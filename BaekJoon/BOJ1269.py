from sys import stdin

N,M = map(int,stdin.readline().split())
A = set(stdin.readline().split())
B = set(stdin.readline().split())

print(len(A-B)+len(B-A))
