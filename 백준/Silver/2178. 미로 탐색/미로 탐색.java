import java.io.*;
import java.util.*;

public class Main {

    static int N, M, ans;
    static List<Integer>[] graph;
    static boolean[][] visited;
    static int[][] map;

    // 상(-1, 0) 하(1, 0) 좌(0, -1) 우(0, 1)
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static class Node{
        int x, y, cnt;
        Node(int x, int y, int cnt){
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N+2][M+2];
        for(int i=1; i<=N; i++){
            String line = br.readLine();
            for(int j=1; j<=M; j++){
                map[i][j] = line.charAt(j-1) - '0';
            }
        }

        visited = new boolean[N+2][M+2];
        bfs(1, 1);
        System.out.println(ans);

    }

    static void bfs(int x, int y){
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(x,y,1));
        visited[x][y] = true;

        while(!q.isEmpty()){
            Node now = q.poll();

            if(now.x == N && now.y == M){
                ans = now.cnt;
            }

            for(int i=0; i<4; i++){
                int nowX = now.x + dx[i];
                int nowY = now.y + dy[i];
                if (!visited[nowX][nowY] && map[nowX][nowY] == 1){
                    visited[nowX][nowY] = true;
                    q.add(new Node(nowX, nowY, now.cnt + 1));
                }
            }

        }
    }

}
