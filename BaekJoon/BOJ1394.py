from sys import stdin

string = stdin.readline().rstrip()
secret = stdin.readline().rstrip()

n = len(string)
m = len(secret)

hash = {string[i]:i+1 for i in range(n)}
ans = 0
g = 1
for i in range(1,m+1):
    ans = (ans+g*hash[secret[m-i]])%900528
    g = g*n%900528

print(ans)
