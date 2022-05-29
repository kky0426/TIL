from sys import stdin


def init(left,right,node):
    if left == right:
        tree[node] = convert(nums[left])
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left,mid,node*2)*init(mid+1,right,node*2+1)
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if left>qRight or right<qLeft:
        return 1

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return query(left,mid,node*2,qLeft,qRight)*query(mid+1,right,node*2+1,qLeft,qRight)

def update(left,right,node,idx,val):
    if idx<left or idx>right:
        return tree[node]

    if left == right:
        tree[node] = convert(val)
        return tree[node]

    mid = (left+right)//2
    tree[node] = update(left,mid,node*2,idx,val)*update(mid+1,right,node*2+1,idx,val)
    return tree[node]

def convert(num):
    num = int(num)
    if num>0:
        return 1
    elif num<0:
        return -1
    else:
        return 0

while True:
    try:
        N,K = map(int,stdin.readline().split())
        nums = list(map(int,stdin.readline().split()))
        tree = [0]*(4*N)
        init(0,N-1,1)
        ans = ""
        for _ in range(K):
            command,s,e = stdin.readline().rstrip().split()
            s = int(s)
            e = int(e)
            if command == 'C':
                nums[s-1] = e
                update(0,N-1,1,s-1,e)
            else:
                num = query(0,N-1,1,s-1,e-1)
                if num>0:
                    ans+="+"
                elif num<0:
                    ans+="-"
                else:
                    ans+="0"
        print(ans)
    except Exception as e:
        break