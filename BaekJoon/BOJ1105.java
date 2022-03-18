import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class BOJ1105 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String left = st.nextToken();
        String right = st.nextToken();

        int ans = 0;

        if (left.length() == right.length()){
            for (int i =0; i<left.length(); i++){
                if(left.charAt(i) != right.charAt(i)){
                    break;
                }else{
                    if (left.charAt(i) == '8') ans++;
                }
            }
        }

        System.out.println(ans);

    }
}
