class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int start = nums.length;
        int end = 0;
        for (int i=0; i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++){
                if (nums[i]>nums[j]){
                    start = Math.min(start,i);
                    end = Math.max(end,j);
                }
            }
        }
        if(start>end) return 0;
        return end-start+1;
    }
}