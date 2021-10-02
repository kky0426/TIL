from sys import stdin

string = stdin.readline().rstrip()
N = len(string)
ans =0
def dfs(string,n):
    if n ==N:
        global ans
        ans+=1
        return

    for ch in char_set:
        idx = ord(ch) - ord("a")
        if dic[idx]==0:
            continue

        if string and string[-1]==ch:
            continue

        dic[idx]-=1
        dfs(string+ch,n+1)
        dic[idx]+=1

char_set=set()
dic = [0]*26
for ch in string:
    dic[ord(ch)-ord("a")]+=1
    char_set.add(ch)

dfs("",0)
print(ans)
