class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = {}
        for num in range(lowLimit,highLimit+1):
            s = 0
            while num>0:
                s+=num%10
                num = num//10
            if s in count:
                count[s]+=1
            else:
                count[s]=1
        return max(count.values())
