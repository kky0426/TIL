dx = [1,0,1]
dy = [0,1,1]
def solution(m, n, board):
    answer = 0
    board = list(map(list,board))
    
    while True:
        board,count = explosion(m,n,board)
        if count == 0:
            break
        answer+=count
        board = down(m,n,board)
    return answer

def down(m,n,board):
    for col in range(n):
        for row in range(m-2,-1,-1):
            if board[row][col] == 0:
                continue
            count = 0
            for  i in range(m-row):
                if board[row+i][col] == 0:
                    count+=1
            if count>0:
                board[row][col],board[row+count][col] = board[row+count][col],board[row][col]
                        
    return board

def explosion(m,n,board):
    queue = set()
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] != 0:
                flag = True
                for k in range(3):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if board[x][y] != board[nx][ny]:
                        flag = False
                if flag:
                    queue.add((x,y))
                    for i in range(3):
                        queue.add((x+dx[i],y+dy[i]))
    count = len(queue)
    while queue:
        x,y = queue.pop()
        board[x][y] = 0
    return board,count
