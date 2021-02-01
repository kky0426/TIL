import collections

n=int(input())

num_list=[num for num in range(1,n+1)]
num_list=collections.deque(num_list)

while(len(num_list)>1):
    num_list.popleft()
    num_list.append(num_list.popleft())

print(num_list[0])
