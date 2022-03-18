import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ20922 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N,K;
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];
        int[] count = new int[100001];
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int answer = 0;
        int left = 0;
        int right = 0;
        while (left<nums.length){
            if(right<nums.length && count[nums[right]]<K){
                count[nums[right]]++;
                right++;
            }else{
                answer = Math.max(answer,right-left);
                count[nums[left]]--;
                left++;
            }
        }
        System.out.println(answer);

    }
}
