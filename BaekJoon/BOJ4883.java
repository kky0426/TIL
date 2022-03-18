import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ4883 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
        int idx = 1;
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            if (N == 0) break;
            int[][] graph = new int[N][3];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                graph[i][0] = Integer.parseInt(st.nextToken());
                graph[i][1] = Integer.parseInt(st.nextToken());
                graph[i][2] = Integer.parseInt(st.nextToken());
            }

            int[][] dp = new int[N+1][3];

            dp[0][0] = Integer.MAX_VALUE;
            dp[0][1] = graph[0][1];
            dp[0][2] = dp[0][1] + graph[0][2];


            for(int i=1; i<N; i++){
                for (int j=0; j<3; j++){
                    if (j == 0){
                        dp[i][j] = Math.min(dp[i-1][j],dp[i-1][j+1])+graph[i][j];
                    }else if (j == 1){
                        int tempA = Math.min(dp[i-1][j],dp[i][j-1]);
                        int tempB = Math.min(dp[i-1][j-1],dp[i-1][j+1]);
                        dp[i][j] = Math.min(tempA,tempB)+graph[i][j];
                    }else{
                        int temp = Math.min(dp[i][j-1],dp[i-1][j]);
                        dp[i][j] = Math.min(temp,dp[i-1][j-1])+graph[i][j];
                    }
                }
            }

            System.out.println(idx+". "+dp[N-1][1]);
            idx++;
        }



    }
}

