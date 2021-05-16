class Solution {
    public int count=0;
    
    public void dfs(int[] nums,int idx,int sum,int target){
            if (idx==nums.length){
                if (sum==target){
                    this.count++;
                }
                return;
            }
            int n=nums[idx];
            dfs(nums,idx+1,sum+n,target);
            dfs(nums,idx+1,sum-n,target);
        }
        
    public int findTargetSumWays(int[] nums, int target) {
        dfs(nums,0,0,target);
        return this.count;
        
    }
}