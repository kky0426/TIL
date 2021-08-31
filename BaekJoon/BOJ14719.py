from sys import stdin

H,N = map(int,stdin.readline().split())

block = list(map(int,stdin.readline().split()))

left = 0
right = N-1
left_max = 0
right_max = 0
ans = 0

while left<right:
    if block[left]>block[right]:
        if right_max<block[right]:
            right_max = block[right]
        else:
            ans+=right_max-block[right]
        right-=1
    else:
        if left_max<block[left]:
            left_max = block[left]
        else:
            ans+=left_max-block[left]
        left+=1

print(ans)
