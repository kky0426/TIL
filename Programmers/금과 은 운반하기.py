def solution(a, b, g, s, w, t):
    answer = -1
    left = 0
    right = 10**9 * 10**5 * 4
    N = len(w)
    while left<=right:
        mid = left+(right-left)//2
        gold=0
        silver=0
        add = 0
        for i in range(N):
            count=mid//(2*t[i])
            if mid%(2*t[i])>=t[i]:
                count+=1
            gold+=min(g[i],w[i]*count)
            silver+=min(s[i],w[i]*count)
            add+=min(g[i]+s[i],w[i]*count)
        
        if gold>=a and silver>=b and add>=a+b:
            right=mid-1
            answer=mid
        else:
            left=mid+1
    return answer
