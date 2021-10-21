import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] nums;
    static int N;
    static boolean[] ans;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        int sum = 0;
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
            sum+=nums[i];
        }
        ans = new boolean[sum+1];
        dfs(0,0);
        int answer = 0;
        for(int i=1; i<=sum; i++){
            if(!ans[i]) answer++;
        }
        System.out.println(answer);
    }

    static void dfs(int idx, int sum){
        if (idx==N){
            if(sum>=0) {
                ans[sum] = true;
            }
            return;
        }else{
            dfs(idx+1,sum+nums[idx]);
            dfs(idx+1,sum-nums[idx]);
            dfs(idx+1,sum);
        }
    }
}