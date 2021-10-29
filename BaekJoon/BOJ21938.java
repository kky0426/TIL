import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N,M;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] grid = new int[N][M];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                int R = Integer.parseInt(st.nextToken());
                int G = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                grid[i][j] = R+G+B;
            }
        }
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if (grid[i][j]/3>=T){
                    grid[i][j] = 1;
                }else{
                    grid[i][j] = 0;
                }
            }
        }
        int ans = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(grid[i][j] == 1){
                    bfs(grid,i,j);
                    ans++;
                }
            }
        }
        System.out.println(ans);

    }
    static void bfs(int[][] grid, int x, int y){
        grid[x][y] = 0;
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        Queue<Integer[]> queue = new LinkedList<>();
        queue.offer(new Integer[]{x,y});
        while(!queue.isEmpty()){
            Integer[] cur = queue.poll();
            for(int i=0; i<4; i++){
                int nx = cur[0]+dx[i];
                int ny = cur[1]+dy[i];
                if(0<=nx && nx<N && 0<=ny && ny<M && grid[nx][ny] == 1){
                    grid[nx][ny] = 0;
                    queue.offer(new Integer[]{nx,ny});
                }
            }
        }
    }
}
