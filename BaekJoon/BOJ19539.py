from sys import stdin

N = int(stdin.readline())
tree = list(map(int,stdin.readline().split()))
s = sum(tree)

if s%3 != 0:
    print("NO")
else:
    count=0
    for n in tree:
        count+=n//2
    if count>=s//3:
        print("YES")
    else:
        print("NO")
