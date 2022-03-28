def convert(time):
    hh, mm, ss = time.split(":")
    h = int(hh) * 3600
    m = int(mm) * 60
    s, ms = map(int, ss.split("."))
    return (h + m + s) * 1000 + ms


def solution(lines):
    answer = 0
    times = []
    N = len(lines)
    for line in lines:
        day, time, duration = line.split()
        t = convert(time)
        d = duration.replace("s", "")
        d = int(float(d) * 1000)
        times.append((t - d + 1, t))

    for i in range(N):
        end = times[i][1]
        count = 0
        for j in range(i, N):
            if end > times[j][0] - 1000:
                count += 1
        answer = max(answer, count)
    return answer