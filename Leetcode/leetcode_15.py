class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        check=set()
        nums.sort()
        for start in range(0,len(nums)-2):
            if nums[start] in check:
                continue
            check.add(nums[start])
            p1=start+1
            p2=len(nums)-1
            while p1<p2:
                if nums[p1]+nums[p2] == -nums[start]:
                    if not [nums[start],nums[p1],nums[p2]] in ans:
                        ans.append([nums[start],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                elif nums[p1]+nums[p2] > -nums[start]:
                    p2-=1
                else:
                    p1+=1
        return ans
