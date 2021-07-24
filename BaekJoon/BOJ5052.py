from sys import stdin

T=int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    nums=[]
    flag=True
    for _ in range(N):
        nums.append(stdin.readline().rstrip())
    nums.sort(reverse=True)

    for i in range(N-1):
        if nums[i].startswith(nums[i+1]):
            flag=False
            break

    if flag:
        print("YES")
    else:
        print("NO")
