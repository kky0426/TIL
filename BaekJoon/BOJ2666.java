import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2666 {

    static int ans = Integer.MAX_VALUE;
    static int[] closet;
    static int N,M;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int openA = Integer.parseInt(st.nextToken());
        int openB = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        closet = new int[M];
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            closet[i] = Integer.parseInt(st.nextToken());
        }
        dfs(openA,openB,0,0);
        System.out.println(ans);
    }

    static void dfs(int openA,int openB, int idx, int count){
        if (idx == M){
            ans = Math.min(ans,count);
            return;
        }
        int moveA = Math.abs(openA-closet[idx]);
        int moveB = Math.abs(openB-closet[idx]);

        dfs(closet[idx],openB,idx+1,count+moveA);
        dfs(openA,closet[idx],idx+1,count+moveB);
    }


}
