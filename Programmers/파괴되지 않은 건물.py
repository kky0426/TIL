def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for typ,r1,c1,r2,c2,degree in skill:
        if typ == 2:
            arr[r1][c1]+=degree
            arr[r1][c2+1]-=degree
            arr[r2+1][c1]-=degree
            arr[r2+1][c2+1]+=degree
        else:
            arr[r1][c1]-=degree
            arr[r1][c2+1]+=degree
            arr[r2+1][c1]+=degree
            arr[r2+1][c2+1]-=degree
    for i in range(len(arr)):
        for j in range(1,len(arr[0])):
            arr[i][j]+=arr[i][j-1]
    
    for j in range(len(arr[0])):
        for i in range(1,len(arr)):
            arr[i][j]+=arr[i-1][j]
    
    for i in range(n):
        for j in range(m):
            if board[i][j]+arr[i][j]>=1:
                answer+=1
    return answer
