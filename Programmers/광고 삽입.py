from collections import deque


def time_to_digit(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def digit_to_time(num):
    h = str(num // 3600)
    num %= 3600
    m = str(num // 60)
    num %= 60
    num = str(num)
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    if len(num) == 1:
        num = "0" + num
    return h + ":" + m + ":" + num


def solution(play_time, adv_time, logs):
    answer = ''
    N = time_to_digit(play_time)
    video = [0] * (N + 1)

    for log in logs:
        start, end = map(time_to_digit, log.split("-"))
        video[start] += 1
        video[end] -= 1

    for i in range(1, N):
        video[i] += video[i - 1]

    length = time_to_digit(adv_time)
    queue = deque()
    s = 0
    for i in range(length):
        queue.append(video[i])
        s += video[i]

    max_sum = s
    ans = 0

    for i in range(length, N):
        s += video[i]
        queue.append(video[i])
        s -= queue.popleft()
        if s > max_sum:
            max_sum = s
            ans = i - length + 1
    answer = digit_to_time(ans)
    return answer