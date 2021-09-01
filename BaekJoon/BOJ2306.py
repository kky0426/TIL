from sys import stdin

string = stdin.readline().rstrip()
N = len(string)

dp = [[-1 for _ in range(N)] for _ in range(N)]

def dna(left,right):
    if left>=right:
        return 0

    if dp[left][right]!=-1:
        return dp[left][right]

    ans = 0
    for k in range(left,right):
        ans = max(ans,dna(left,k)+dna(k+1,right))

    if (string[left] == 'a' and string[right] == 't') or (string[left] == 'g' and string[right] == 'c'):
        ans = max(ans,dna(left+1,right-1)+2)

    dp[left][right] = ans
    return dp[left][right]

dna(0,N-1)
print(dp[0][N-1])
