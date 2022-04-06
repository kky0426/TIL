from sys import stdin

while True:
    try:
        hole = int(stdin.readline())
        hole*= 10000000
        N = int(stdin.readline())
        nums = [int(stdin.readline()) for _ in range(N)]
        nums.sort()
        flag = False
        left = 0
        right = N-1
        while left<right:
            if nums[left]+nums[right] == hole:
                print("yes {} {}".format(nums[left],nums[right]))
                flag = True
                break
            elif nums[left]+nums[right]>hole:
                right-=1
            else:
                left+=1
        if not flag:
            print("danger")
    except:
        break
