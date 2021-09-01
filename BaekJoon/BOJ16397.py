from sys import stdin
from collections import deque

def A(num):
    return num+1

def B(num):
    num*=2
    if num>99999:
        return 1000000
    num = list(str(num))
    if num[0]!='0': num[0] = int(num[0]) - 1
    return int("".join(map(str,num)))

def bfs(start):
    visit = set()
    queue = deque()
    visit.add(start)
    queue.append((start,0))

    while queue:
        num,count = queue.popleft()
        if num == G:
            return count
        a_num = A(num)
        b_num = B(num)
        if a_num<=99999 and a_num not in visit:
            queue.append((a_num,count+1))
            visit.add(a_num)
        if b_num<=99999 and b_num not in visit:
            queue.append((b_num,count+1))
            visit.add(b_num)

    return float("inf")

N,T,G = map(int,stdin.readline().split())

btn = bfs(N)
print(btn if btn<=T else "ANG" )
