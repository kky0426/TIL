from sys import stdin

bracket = stdin.readline().rstrip()


def solve(bracket):
    left,right,s = 0,0,0
    for i in range(len(bracket)):
        if bracket[i] == "(":
            left+=1
            s+=1
        else:
            right+=1
            s-=1

        if s<0:
            return right
        if s == 0:
            left = 0
    return left

print(solve(bracket))