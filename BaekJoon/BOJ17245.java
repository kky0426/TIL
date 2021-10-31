import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int[][] grid = new int[N][N];
        long sum = 0;
        for(int i=0; i<N ; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                sum+=grid[i][j];
            }
        }
        Map<Integer,Integer> map = new HashMap<>();
        map.forEach((key,value)->{

        });
        map.containsKey()
        long left = 0;
        long right = sum+1;
        long ans = 0;
        while(left<=right){
            long mid = left+(right-left)/2;
            if(check(grid,mid)>=(double)sum/2){
                ans = mid;
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        Map<Integer,Integer> map = new HashMap<>();
        map.si
        System.out.println(ans);
    }

    static long check(int[][] grid,long air){
        long count = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if (grid[i][j] > air){
                    count+=air;
                }else{
                    count+=grid[i][j];
                }
            }
        }
        return count;
    }
}
