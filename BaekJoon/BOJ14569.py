from sys import stdin

N = int(stdin.readline())
subjects = [set(list(map(int,stdin.readline().split()))[1:]) for _ in range(N)]

M = int(stdin.readline())
students = [set(list(map(int,stdin.readline().split()))[1:]) for _ in range(M)]

for student in students:
    ans = 0
    for subject in subjects:
        if student&subject == subject:
            ans+=1
    print(ans)
