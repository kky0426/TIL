import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class BOJ13164 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int[] diff = new int[N-1];
        for(int i=0; i<N-1; i++){
            diff[i] = nums[i+1]-nums[i];
        }
        Arrays.sort(diff);
        int ans = 0;
        for(int i=0; i<N-K; i++){
            ans+=diff[i];
        }
        System.out.println(ans);

    }
}
