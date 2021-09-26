from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

frame = []
student = [1001]*101
for time in range(M):
    if student[nums[time]] != 1001:
        for i in range(len(frame)):
            if frame[i][0] == nums[time]:
                frame[i][1] += 1
                student[nums[time]] += 1
    else:
        if len(frame) >= N:
            min_value = min(student)
            for i in range(len(frame)):
                if frame[i][1] == min_value:
                    student[frame[i][0]] = 1001
                    frame.pop(i)
                    break

        frame.append([nums[time],1])
        student[nums[time]]=1

ans = []
for i,v in frame:
    ans.append(i)
ans.sort()
for a in ans:
    print(a,end=" ")
