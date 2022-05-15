from sys import stdin

nums = list(map(int,stdin.readline().split()))

output = []
ans = 0

def check():
    global ans
    count = 0
    for i in range(10):
        if output[i] == nums[i]:
            count+=1
    if count>=5:
        ans+=1

def solve(idx):
    if idx == 10:
        check()
        return

    for i in range(1,6):
        if idx>1 and output[idx-1] == output[idx-2] == i:
            continue
        output.append(i)
        solve(idx+1)
        output.pop()

solve(0)
print(ans)
