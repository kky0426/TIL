def solution(brown, yellow):
    inBox=[]
    for i in range(1,yellow+1):
        if yellow%i==0 and i>=yellow//i:
            inBox.append((i,yellow//i))
    
    for row,col in inBox:
        count = 2*row + 2*col +4
        if count == brown:
            return [row+2,col+2]
        
