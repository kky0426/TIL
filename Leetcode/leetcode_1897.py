class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for word in words:
            for i in range(len(word)):
                if word[i] in dic:
                    dic[word[i]]+=1
                else:
                    dic[word[i]]=1
        for k,v in dic.items():
            if v%len(words) !=0:
                return False
        return True
