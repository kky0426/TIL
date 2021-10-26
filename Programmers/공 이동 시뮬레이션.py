def solution(n, m, x, y, queries):
    top,left,right,bottom = x,y,y,x;
    queries.reverse()
    answer = 0
    for num,dx in queries:
        if num == 0:
            current = min(right+dx,m-1)                   
            if left == 0:
                right = current
            else:
                left = left+dx
                right = current
    
        elif num == 1:
            current = max(0,left - dx)            
            if right == m-1:
                left = current
            else:
                left = current
                right = right-dx
            
        elif num == 2:
            current = min(n-1,bottom+dx)
            if top == 0:
                bottom = current
            else:
                top = top+dx
                bottom = current
                
        elif num == 3:
            current = max(0,top-dx)            
            if bottom == n-1:
                top = current
            else:
                top = current
                bottom = bottom-dx
     
        if left>m-1 or right<0 or top>n-1 or bottom<0:
            answer = 0
            break
        else:
            answer = ((bottom-top)+1)*((right-left)+1)
    return answer
