class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mW=0
        mH=0
        hor = sorted(horizontalCuts)
        ver = sorted(verticalCuts)
        for i in range(len(hor)):
            if i==len(hor)-1:
                mH=max(mH,h-hor[i])
            else:
                mH=max(mH,hor[i+1]-hor[i])
        mH=max(mH,hor[0])
        for i in range(len(ver)):
            if i==len(ver)-1:
                mW=max(mW,w-ver[i])
            else:
                mW=max(mW,ver[i+1]-ver[i])
        mW=max(mW,ver[0]) 
        return (mW*mH)%(10**9+7)
