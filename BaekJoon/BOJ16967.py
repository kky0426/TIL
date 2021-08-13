from sys import stdin

H,W,X,Y = map(int,stdin.readline().split())

A=[[0 for _ in range(W)] for _ in range(H)]
B=[]

for _ in range(H+X):
    B.append(list(map(int,stdin.readline().split())))

for i in range(len(B)):
    for j in range(len(B[0])):
        if X<=i<H and Y<=j<W:
            A[i][j] = B[i][j] - A[i-X][j-Y]
        elif i<X and j<W:
            A[i][j] = B[i][j]
        elif i<H and j<Y:
            A[i][j] = B[i][j]

for i in range(H):
    for j in range(W):
        print(A[i][j],end=' ')
    print()
