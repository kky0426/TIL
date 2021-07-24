from sys import stdin
N=int(stdin.readline())
dic={}

for _ in range(N):
    name,log=stdin.readline().split()
    if name in dic:
        dic[name]+=1
    else:
        dic[name]=1

ans=[]
for k,v in dic.items():
    if v%2!=0:
        ans.append(k)
ans.sort(reverse=True)

for p in ans:
    print(p)
