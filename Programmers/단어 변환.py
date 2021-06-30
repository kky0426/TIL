from collections import defaultdict
from collections import deque
def compare(word1,word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count+=1
    return count

def solution(begin, target, words):
    if not target in words:
        return 0
    
    answer = 0
    words.append(begin)
    dic=defaultdict(list)
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i==j:
                continue
            if compare(words[i],words[j]) == len(words[i])-1:
                dic[words[i]].append(words[j])
    queue = deque()
    queue.append((begin,0))
    visit=set()
    while queue:
        node,answer= queue.popleft()
        visit.add(node)
        if node == target:
            return answer
        
        for word in dic[node]:
            if not word in visit:
                queue.append((word,answer+1))
                
