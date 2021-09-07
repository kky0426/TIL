def solution(key, lock):
    N = len(lock)
    M = len(key)

    for _ in range(4):
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                if insert(key, lock, N, M, i, j):
                    return True
        key = rotate(key)
        
    return False


def insert(key, lock, N, M, x, y):
    length = 2 * M + N-2
    background = [[0 for _ in range(length)] for _ in range(length)]



    # key 넣기
    for i in range(M):
        for j in range(M):
            background[x+i][y+j] = key[i][j]

    # lock 넣기
    for i in range(M-1, M+N-1):
        for j in range(M-1, M+N-1):
            background[i][j] += lock[i -M+1][j - M+1]
            if background[i][j] !=1 :
                return False
    return True
