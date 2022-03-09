from sys import stdin

N = int(stdin.readline())
string=["m","o","o"]
ans = ""

def solve(n,k,l):
    length = 2*l+k+3
    if n<=3:
        print(string[n-1])
        exit(0)

    if length<n:
        solve(n,k+1,length)
    else:
        if n>l and n<=l+k+3:
            if n-l!=1:
                print("o")
            else:
                print("m")
            exit(0)
        else:
            solve(n-(l+k+3),1,3)

solve(N,1,3)



