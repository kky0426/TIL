import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ1623 {
    static int N;
    static ArrayList<ArrayList<Integer>> tree;
    static boolean[] visit;
    static int[][] dp;
    static ArrayList<Integer> ans;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        tree = new ArrayList<>();
        for(int i=0;i<=N;i++){
            tree.add(new ArrayList<>());
        }
        dp = new int[N+1][2];
        visit = new boolean[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++){
            dp[i+1][1] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N-1;i++){
            int num = Integer.parseInt(st.nextToken());
            tree.get(num).add(i+2);
        }
        dfs(1);
        System.out.println(dp[1][1]+" "+dp[1][0]);
        ans = new ArrayList<>();
        ArrayList<Integer> ans = trace(1, 1);
        ans.sort(null);
        for (Integer num: ans){
            System.out.print(num+" ");
        }
        System.out.println(-1);
        ans.clear();
        ans = trace(1,0);
        ans.sort(null);
        for(Integer num:ans){
            System.out.print(num+" ");
        }
        System.out.println(-1);
    }

    public static void dfs(int cur){
        visit[cur] = true;
        for(Integer node : tree.get(cur)){
            dfs(node);
            dp[cur][1]+=dp[node][0];
            if (dp[node][0]>dp[node][1]){
                visit[node] = false;
                dp[cur][0] += dp[node][0];
            }else{
                visit[node] = true;
                dp[cur][0] += dp[node][1];
            }
        }
    }

    public static ArrayList<Integer> trace(int node,int is_come){
        ArrayList<Integer> ans = new ArrayList<>();
        Queue queue = new LinkedList();
        queue.offer(new int[]{node, is_come});
        while (!queue.isEmpty()){
            int[] element = (int[]) queue.poll();
            int come = element[1];
            if(come == 1){
                ans.add(element[0]);
            }
            for (Integer child : tree.get(element[0])){
                if(come == 1){
                    queue.offer(new int[]{child,0});
                }else{
                    if(visit[child] == true){
                        queue.offer(new int[]{child,1});
                    }else{
                        queue.offer(new int[]{child,0});
                    }
                }
            }
        }
        return ans;
    }
}
