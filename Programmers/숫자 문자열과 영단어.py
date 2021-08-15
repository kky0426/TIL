def solution(s):
    answer = ""
    dic={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5",
        "six":"6","seven":"7","eight":"8","nine":"9"}
    temp=""
    for ch in s:
        if ch.isdigit():
            answer+=ch
        else:
            temp+=ch
        
        if temp and temp in dic:
            answer+=dic[temp]
            temp = ""
    return int(answer)
