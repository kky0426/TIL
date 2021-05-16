class Solution {
    public int numSquares(int n) {
        int[] dp= new int[n+1];
        Arrays.fill(dp,10001);
        int idx=1;
        while((int)Math.pow(idx,2)<=n){
            dp[(int)Math.pow(idx,2)]=1;
            idx++;
        }
        
        for (int i=2;i<dp.length;i++){
            for (int j=1;j<idx;j++){
                if ((int)Math.pow(j,2)>i) break;
                dp[i]=Math.min(dp[i],dp[i-(int)Math.pow(j,2)]+1);
            }
        }
        
        return dp[n];
    }
}
