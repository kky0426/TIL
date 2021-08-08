from sys import stdin

n=0
dic={}

while True:
    name = stdin.readline().rstrip()
    if not name:
        break
    if name in dic:
        dic[name]+=1
    else:
        dic[name]=1
    n+=1

for k,v in sorted(dic.items(),key=lambda x:x[0]):
    print(k,"{:.4f}".format(round(v/n*100,4)))
