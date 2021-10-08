def solution(name):
    answer = 0
    N = len(name)
    move = N-1
    for i,ch in enumerate(name):
        answer+= min(ord(ch)-ord('A'),ord('Z')-ord(ch)+1)
        
        next_idx = i+1
        while next_idx<N and name[next_idx]=='A':
            next_idx+=1
        
        move = min(move,i+i+N-next_idx)
    answer+=move
    return answer
