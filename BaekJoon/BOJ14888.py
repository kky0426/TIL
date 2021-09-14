from sys import stdin
from collections import deque
from itertools import permutations
def calculation(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if a<0:
            return -(-a//b)
        return a//b
"""
def permutation(arr,n):
    for i in range(len(arr)):
        if n==1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next
"""

N =int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
plus,minus,product,divition = map(int,stdin.readline().split())
operation=[]

while plus+minus+product+divition>0:
    if plus>0:
        operation.append("+")
        plus-=1
    if minus>0:
        operation.append("-")
        minus-=1
    if product>0:
        operation.append("*")
        product-=1
    if divition>0:
        operation.append("/")
        divition-=1
visit = set()
ans = []
for op in permutations(operation,N-1):
    queue = deque(nums)
    op = deque(op)
    if "".join(op) in visit:
        continue
    visit.add("".join(op))

    while op:
        a = queue.popleft()
        b = queue.popleft()
        o = op.popleft()
        res = calculation(a,b,o)
        queue.appendleft(res)
    ans.append(queue[0])

print(max(ans))
print(min(ans))
