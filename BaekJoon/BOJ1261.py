from sys import stdin
import heapq

M,N = map(int,stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
def bfs():
    visit[0][0] = True
    queue = []
    queue.append((0,0,0))
    ans = float("inf")
    while queue:
        count,x,y = heapq.heappop(queue)
        if x==N-1 and y==M-1:
            return count

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if board[nx][ny] == 1:
                    visit[nx][ny] = True
                    heapq.heappush(queue,(count+1,nx,ny))
                else:
                    visit[nx][ny]=True
                    heapq.heappush(queue,(count,nx,ny))
    return ans

ans = bfs()
print(ans)
