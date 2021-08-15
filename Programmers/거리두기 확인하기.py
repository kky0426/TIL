from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(board,x,y):
    queue = deque()
    queue.append((x,y,0))
    visit = set()
    visit.add((x,y))
    while queue:
        x,y,dis = queue.popleft()
        if board[x][y] == 'P' and 0<dis<=2:
            return False
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and (nx,ny) not in visit and board[nx][ny] !='X':
                queue.append((nx,ny,dis+1))
                visit.add((nx,ny))
    return True

def solution(places):
    answer = []
    for board in places:
        flag = True
        for i in range(5):
            if not flag: break
            for j in range(5):
                if board[i][j] =='P':
                    if not bfs(board,i,j):
                        flag = False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer
