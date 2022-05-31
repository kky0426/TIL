from sys import stdin

N,M = map(int,stdin.readline().split())

tree = [0]*(4*N)
lazy = [0]*(4*N)

def query(left,right,node,qLeft,qRight):
    propagation(left,right,node)
    if qLeft>right or qRight<left:
        return 0

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return query(left,mid,node*2,qLeft,qRight)+query(mid+1,right,node*2+1,qLeft,qRight)

def propagation(left,right,node):
    if lazy[node]%2 != 0:
        tree[node] = (right-left+1)-tree[node]
        if left!=right:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

def update(left,right,node,uLeft,uRight):
    propagation(left,right,node)

    if uLeft>right or uRight<left:
        return

    if uLeft<=left and right<=uRight:
        tree[node] =(right-left+1) - tree[node]
        if left!=right:
            lazy[node*2]+=1
            lazy[node*2+1]+=1
        return

    mid = (left+right)//2
    update(left,mid,node*2,uLeft,uRight)
    update(mid+1,right,node*2+1,uLeft,uRight)
    tree[node] = tree[node*2]+tree[node*2+1]

for _ in range(M):
    o,s,t = map(int,stdin.readline().split())
    if o == 0:
        update(0,N-1,1,s-1,t-1)
    else:
        print(query(0,N-1,1,s-1,t-1))
