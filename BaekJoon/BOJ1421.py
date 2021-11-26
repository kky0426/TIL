from sys import stdin

N,C,W = map(int,stdin.readline().split())

wood = [int(stdin.readline()) for _ in range(N)]

ans = 0

end = max(wood)

for length in range(1,end+1):
    s = 0
    for w in wood:
        if w<length:
            continue
        count = w//length
        if w%length == 0:
            cut = w//length -1
        else:
            cut = w//length

        if (count*W*length - cut*C > 0):
            s+=count*W*length - cut*C

    ans = max(ans,s)

print(ans)
