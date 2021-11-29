from sys import stdin

N,r,c = map(int,stdin.readline().split())

count = 0
while N>1:
    size = (2**N)//2
    if r<size and c<size:
        pass
    elif r<size and c>=size:
        c-=size
        count+=size**2
    elif r>=size and c<size:
        r-=size
        count+=size**2 * 2
    else:
        c-=size
        r-=size
        count+=size**2 * 3
    N-=1

print(count+2*r+1*c)
