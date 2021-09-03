def solution(n, t, m, timetable):
    answer = ''
    ans = 0
    timetable.sort()
    new_time = []
    for time in timetable:
        time_ = int(time[:2])*60 + int(time[3:])
        new_time.append(time_)
    
    bus = [540+(i*t) for i in range(n)]
    idx = 0
    for current in bus:
        count = 0
        while count<m and idx<len(new_time) and new_time[idx]<=current:
            count+=1
            idx+=1
        if count == m:
            ans = new_time[idx-1]-1
        else:
            ans = current
    
    hour = str(ans//60)
    if len(hour)<2: hour = "0"+hour
    minute = str(ans%60)
    if len(minute)<2: minute = "0"+minute
    answer=hour+":"+minute
    return answer
