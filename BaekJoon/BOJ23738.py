from sys import stdin

dic = {"B":"v","E":"ye","H":"n","P":"r","C":"s","Y":"u","X":"h"}

string = stdin.readline().rstrip()

for k,v in dic.items():
    string = string.replace(k,v)

print(string.lower())
