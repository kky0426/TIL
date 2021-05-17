def solution(numbers, hand):
    answer = ''
    key={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),'*':(3,0),0:(3,1),'#':(3,2)}
    cur_r=key['*']
    cur_l=key['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            cur_l=key[num]
        elif num in [3,6,9]:
            answer+='R'
            cur_r=key[num]
        else:
            x,y=key[num]
            if (abs(cur_r[0]-x)+abs(cur_r[1]-y))<(abs(cur_l[0]-x)+abs(cur_l[1]-y)):
                answer+='R'
                cur_r=key[num]
            elif (abs(cur_r[0]-x)+abs(cur_r[1]-y))>(abs(cur_l[0]-x)+abs(cur_l[1]-y)):
                answer+='L'
                cur_l=key[num]
            else:
                if hand=='right':
                    answer+='R'
                    cur_r=key[num]
                else:
                    answer+='L'
                    cur_l=key[num]
    return answer
