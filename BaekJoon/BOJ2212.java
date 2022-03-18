import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2212 {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        if (K>=N){
            System.out.println(0);
        }else {
            int[] num = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                num[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(num);
            int[] diff = new int[N - 1];
            for (int i = 0; i < N - 1; i++) {
                diff[i] = num[i + 1] - num[i];
            }
            Arrays.sort(diff);

            int ans = 0;
            for (int i = 0; i < N - K; i++) {
                ans += diff[i];
            }
            System.out.println(ans);
        }
    }
}
