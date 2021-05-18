class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] sumList = new int[nums.length];
        int count = 0;
        sumList[0]=nums[0];
        for(int i=1; i<nums.length; i++){
            sumList[i]=sumList[i-1]+nums[i];
        }
        
        for(int i=0; i<nums.length;i++){
            if (sumList[i]==k) count++;
            for(int j=0; j<i;j++){
                if (sumList[i]-sumList[j]==k) count++;
            }
        }
        return count;
    }
   
}