from sys import stdin

N = int(stdin.readline())

strings = []

for _ in range(N):
    strings.append(stdin.readline().rstrip())

for string in strings:
    left = 0
    right = len(string)-1
    left_count = 0
    while left<=right and left_count<2:
        if string[left] == string[right]:
            left+=1
            right-=1
        elif string[left+1] == string[right]:
            left+=1
            left_count+=1
        else:
            left+=1
            right-=1
            left_count+=2

    left = 0
    right = len(string) - 1
    right_count = 0
    count=0
    while left <= right and right_count<2:
        if string[left] == string[right]:
            left += 1
            right -= 1
        elif string[left] == string[right-1]:
            right -= 1
            right_count+=1
        else:
            left+=1
            right-=1
            right_count+=2

    if left_count==0 and right_count == 0:
        print(0)
    elif left_count<2 or right_count<2:
        print(1)
    else:
        print(2)
