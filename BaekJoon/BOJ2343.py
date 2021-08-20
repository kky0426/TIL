from sys import stdin

N,M = map(int,stdin.readline().split())

lesson = list(map(int,stdin.readline().split()))

left = max(lesson)
right = 10001*N//M
ans=0
while left<=right:
    mid = left+(right-left)//2

    count = 1
    time = 0
    for second in lesson:
        if time+second<=mid:
            time+=second
        else:
            count+=1
            time = second

    if count<=M:
        ans = mid
        right=mid-1
    else:
        left=mid+1
        
print(ans)
