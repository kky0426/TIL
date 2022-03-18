import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2304 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<Tower> towers = new ArrayList<>();

        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            towers.add(new Tower(x,h));
        }
        Collections.sort(towers);
        int ans = 0;
        int idx = 0;
        Tower current = towers.get(0);
        for(int i=1; i<N; i++){
            if (current.h <= towers.get(i).h){
                ans+=(towers.get(i).x - current.x)*current.h;
                current = towers.get(i);
                idx = i;
            }
        }
        current = towers.get(N-1);
        for(int i=0; i<N-idx; i++){
            if(current.h <= towers.get(N-i-1).h){
                ans+=(current.x-towers.get(N-i-1).x)*current.h;
                current = towers.get(N-i-1);
            }
        }
        ans+= current.h;
        System.out.println(ans);
    }

    static class Tower implements Comparable<Tower>{
        int x;
        int h;

        public Tower(int x, int h){
            this.x = x;
            this.h = h;
        }

        @Override
        public int compareTo(Tower o) {
            return this.x-o.x;
        }
    }


}
