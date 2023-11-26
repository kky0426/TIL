from collections import deque


def solution(land):
    answer = 0
    N = len(land)
    M = len(land[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(visit, x, y, index):
        count = 1
        queue = deque()
        queue.append((x, y))
        visit[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            land[cx][cy] = index
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1 and not visit[nx][ny]:
                    queue.append((nx, ny))
                    visit[nx][ny] = True
                    count += 1
        return count

    dic = {}
    visit = [[False for _ in range(M)] for _ in range(N)]
    index = 2
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visit[i][j]:
                oil = bfs(visit, i, j, index)
                dic[index] = oil
                index += 1

    for j in range(M):
        oils = set()
        ans = 0
        for i in range(N):
            if land[i][j] > 0:
                oils.add(land[i][j])

        for e in oils:
            ans += dic[e]

        answer = max(answer, ans)
    return answer