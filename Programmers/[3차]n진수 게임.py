def jinbup(num,n):
    module_num=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n_str=''
    if num==0:
        return '0'
    while num>0:
        n_str=module_num[num%n]+n_str
        num=num//n
    return n_str

def solution(n, t, m, p):
    answer = ''
    total=''
    for i in range(t*m):
        total+=jinbup(i,n)
    
    for j in range(p,t*m+1,m):
        answer+=total[j-1]
        
    
    return answer
