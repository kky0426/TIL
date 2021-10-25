import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] nums;
    static boolean[] visit;
    static ArrayList<Integer> ans;
    static int start;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ans = new ArrayList<>();
        nums = new int[N+1];
        visit = new boolean[N+1];
        for(int i=1; i<=N; i++){
            st = new StringTokenizer(br.readLine());
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=1; i<=N; i++){
            visit[i] = true;
            start = i;
            dfs(i);
            visit[i] = false;
        }
        Collections.sort(ans);
        System.out.println(ans.size());
        for(int num:ans){
            System.out.println(num);
        }
    }

    static void dfs(int idx){
        if (!visit[nums[idx]]){
            visit[nums[idx]] = true;
            dfs(nums[idx]);
            visit[nums[idx]]=false;
        }
        if (nums[idx] == start){
            ans.add(start);
        }
    }
}
