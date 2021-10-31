from sys import stdin

string = list(stdin.readline().rstrip())

window = string.count("a")
N = len(string)
string.extend(string)

left = 0
right = 0
ans = N-window
count = 0
while right<N+window:
    if string[right] == 'b':
        count+=1

    if right-left<window:
        right+=1
    else:
        if string[left] == 'b':
            count-=1
        left+=1
        right+=1
        ans = min(ans,count)
print(ans)
