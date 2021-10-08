def rotate(x1, y1, x2, y2, board):
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    
    temp = board[x1][y1]
    ans = temp
    #up
    for i in range(x1, x2):
        board[i][y1] = board[i + 1][y1]
        ans = min(ans,board[i+1][y1])
    #left
    for i in range(y1, y2):
        board[x2][i] = board[x2][i+1]
        ans = min(ans,board[x2][i+1])
    #down
    for i in range(x2, x1, -1):
        board[i][y2] = board[i - 1][y2]
        ans = min(ans,board[i-1][y2])
    #right
    for i in range(y2, y1, -1):
        board[x1][i] = board[x1][i - 1]
        ans = min(ans,board[x1][i-1])
    board[x1][y1 + 1] = temp
    
    return ans


def solution(rows, columns, queries):
    answer = []
    board=[[columns*i+j+1 for j in range(columns)] for i in range(rows)]
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(x1,y1,x2,y2,board))
        
    return answer
