from sys import stdin

dic = {"q":(0,0),"w":(0,1),"e":(0,2),"r":(0,3),"t":(0,4),"y":(0,5),"u":(0,6),"i":(0,7),"o":(0,8),"p":(0,9),
       "a":(1,0),"s":(1,1),"d":(1,2),"f":(1,3),"g":(1,4),"h":(1,5),"j":(1,6),"k":(1,7),"l":(1,8),
        "z":(2,0),"x":(2,1),"c":(2,2),"v":(2,3),"b":(2,4),"n":(2,5),"m":(2,6)
       }

T = int(stdin.readline())

def get_dis(word,compare):
    dis = 0
    for i in range(len(word)):
        dis+=abs(dic[word[i]][0]-dic[compare[i]][0]) + abs(dic[word[i]][1]-dic[compare[i]][1])
    return dis

for _ in range(T):
    word,n = stdin.readline().split()
    n = int(n)
    words = []
    for _ in range(n):
        compare = stdin.readline().rstrip()
        dis = get_dis(word,compare)
        words.append((compare,dis))
    words.sort(key=lambda x:(x[1],x[0]))
    for ans,dis in words:
        print(ans,dis)
