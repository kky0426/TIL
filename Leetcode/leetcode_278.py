# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        
        start=1
        end=n
        while start<end:
            mid=(start+end)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return start
