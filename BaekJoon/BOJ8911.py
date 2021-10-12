from sys import stdin

head = [(-1,0),(0,1),(1,0),(0,-1)]

T = int(stdin.readline())
for _ in range(T):
    command = stdin.readline().rstrip()
    x,y,d = 0,0,0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for ch in command:
        if ch == 'F':
            x=x+head[d][0]
            y=y+head[d][1]
      

        elif ch == 'B':
            x = x - head[d][0]
            y = y - head[d][1]

        elif ch == 'L':
            d = (d-1)%4
        elif ch == 'R':
            d = (d+1)%4
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(abs(max_x-min_x)*abs(max_y-min_y))
