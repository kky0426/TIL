import java.util.*;

class Node{
    public int x;
    public int y;
    
    public Node(int x,int y){
        this.x = x;
        this.y = y;
    }
}

class Solution {

    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};
    int M;
    int N;
    public int[] solution(int m, int n, int[][] picture) {
        this.M = m;
        this.N = n;
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean visit[][] = new boolean[m][n];
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (!visit[i][j] && picture[i][j]>0){
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea,bfs(i,j,visit,picture));
                    numberOfArea++;
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    public int bfs(int x,int y,boolean[][] visit,int[][] picture){
        Queue<Node> queue = new LinkedList<>();
        Node node = new Node(x,y);
        queue.offer(node);
        visit[x][y] = true;
        int count = 1;
        while (!queue.isEmpty()){
            Node next = queue.poll();
            for (int i=0;i<4;i++){
                int nx = next.x+dx[i];
                int ny = next.y+dy[i];
                if(0<=nx && nx<M && 0<=ny && ny<N){
                    if (picture[nx][ny] == picture[x][y] && !visit[nx][ny]){
                        visit[nx][ny] = true;
                        queue.offer(new Node(nx,ny));
                        count++;
                    }
                }
            }
        }
        return count;
    }
 
}
