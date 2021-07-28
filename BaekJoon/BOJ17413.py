from sys import stdin

string = stdin.readline().rstrip()
string=string.replace(" ",'*')
string=string.replace("<"," <")
string=string.replace(">","> ")
string=string.split()

ans=[]
for ch in string:
    if '>' in ch:
        ans.append(ch.replace("*"," "))
    else:
        ans.extend(ch.split("*"))
result=""
for i in range(len(ans)):
    if '>' in ans[i]:
        result+=ans[i]
    else:
        if i>0 and '>' in ans[i-1]:
            result+="".join(reversed(ans[i]))
        else:
            if i>0:
                result+=" "
            result+="".join(reversed(ans[i]))
print(result)
