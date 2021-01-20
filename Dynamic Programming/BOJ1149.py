n=int(input())

ary_r=[]
ary_g=[]
ary_b=[]

for i in range(n):
    r,g,b=map(int,input().split())
    ary_r.append(r)
    ary_g.append(g)
    ary_b.append(b)

dp=[[0 for _ in range(3)] for _ in range(n+1)]

dp[1][0]=ary_r[0]
dp[1][1]=ary_g[0]
dp[1][2]=ary_b[0]

for j in range(2,n+1):
    dp[j][0]= min(dp[j-1][1],dp[j-1][2]) + ary_r[j-1]
    dp[j][1]= min(dp[j-1][0],dp[j-1][2]) + ary_g[j-1]
    dp[j][2]= min(dp[j-1][0],dp[j-1][1]) + ary_b[j-1]

print(min(dp[n]))
