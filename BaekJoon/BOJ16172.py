from sys import stdin

string = stdin.readline().rstrip()

for i in range(10):
    string = string.replace(str(i),"")

K = stdin.readline().rstrip()
print(1 if K in string else 0)