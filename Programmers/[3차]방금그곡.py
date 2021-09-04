def solution(m, musicinfos):
    answer = "(None)"
    ans = []
    m = m.replace("C#","c").replace("D#","d").replace("G#","g").replace("A#","a").replace("F#","f")
    max_duration = 0
    for i,words in enumerate(musicinfos):
        start,end,name,code = words.split(",")
        code = code.replace("C#","c").replace("D#","d").replace("G#","g").replace("A#","a").replace("F#","f")
        l = len(code)
        duration = getDuration(start,end)
            
        play = ""
        for i in range(duration):
            play+=code[i%l]
        
        if m in play:
            if duration>max_duration:
                answer = name
                max_duration = duration
    return answer
       


def getDuration(start,end):
    start_H = int(start[:2])
    start_M = int(start[3:])
    end_H = int(end[:2])
    end_M = int(end[3:])
    
    time_s = 60*start_H + start_M
    time_e = 60*end_H + end_M
    
    return (time_e-time_s)
