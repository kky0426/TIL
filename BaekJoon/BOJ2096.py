from sys import stdin

N = int(stdin.readline())

min_left=0
min_mid=0
min_right=0
min_left_pre=0
min_mid_pre=0
min_right_pre=0

max_left=0
max_mid= 0
max_right=0
max_left_pre=0
max_mid_pre= 0
max_right_pre=0

for _ in range(N):
    left,mid,right = map(int,stdin.readline().split())
    #왼쪽
    min_left = min(min_left_pre,min_mid_pre) + left
    max_left = max(max_left_pre,max_mid_pre) + left
    #중간
    min_mid = min(min_left_pre,min_mid_pre,min_right_pre) + mid
    max_mid = max(max_left_pre,max_mid_pre,max_right_pre) + mid
    #오른쪽
    min_right = min(min_right_pre,min_mid_pre) + right
    max_right = max(max_right_pre,max_mid_pre) + right

    min_left_pre = min_left
    min_mid_pre = min_mid
    min_right_pre = min_right
    max_left_pre = max_left
    max_mid_pre = max_mid
    max_right_pre = max_right

print(max(max_left,max_mid,max_right),min(min_left,min_mid,min_right))
\
