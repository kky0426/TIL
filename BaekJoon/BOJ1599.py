from sys import stdin

N = int(stdin.readline())

words = [stdin.readline().rstrip().replace("ng",'N') for _ in range(N)]

dic = {"a":1,"b":2,"k":3,"d":4,"e":5,"g":6,"h":7,"i":8,"l":9,"m":10
          ,"n":11,"N":12,"o":13,"p":14,"r":15,"s":16,"t":17,"u":18,"w":19,"y":20}

def compare(word1,word2):
    N = min(len(word1),len(word2))
    for i in range(N):
        if word1[i] == word2[i]:
            continue
        if dic[word1[i]]>dic[word2[i]]:
            return 1
        else:
            return -1
    if len(word1)>len(word2):
        return 1
    else:
        return -1

for i in range(N):
    for j in range(i+1,N):
        if compare(words[i],words[j]) == 1:
            words[i],words[j] = words[j],words[i]

for i in range(N):
    words[i] = words[i].replace("N","ng")
    print(words[i])
